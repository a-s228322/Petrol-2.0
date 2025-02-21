from io import BytesIO
import pandas as pd
from fastapi import FastAPI, Request, UploadFile, File, Response, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sklearn.neighbors import KNeighborsClassifier
import pickle
import numpy as np
from starlette.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def model_prediction(buffer):

    reg_model_filename = "saved_models/pickle_regression_model.pkl"
    with open(reg_model_filename, "rb") as file:
        reg_model = pickle.load(file)

    chemisrty_classes = [1, 2, 3, 4, 5, 6]
    percent_rate = [5, 10, 15, 20]
    # input_excel = "input_user_data/input_data.xlsx"
    df = pd.read_excel(buffer)

    # output df to excel concatenated with class and chemistry percent rate
    df_output = df.sample(frac=1).sample(n=5)
    df_output["класс химии"] = 0
    df_output["процент химии"] = 0
    for index in range(5):
        data = pd.DataFrame(df_output.iloc[index, :]).transpose()
        prediction_dict = dict()
        for chm_class in np.sort(chemisrty_classes):
            data["класс химии"] = chm_class
            for rate in np.sort(percent_rate):
                data["процент химии"] = rate
                predictions = reg_model.predict(data).values
                prediction_dict[f"{chm_class}_{rate}_{index}"] = predictions[0]

        df_predictions = pd.DataFrame(prediction_dict.values())
        df_predictions["class"] = [int(key.split('_')[0]) for key in prediction_dict.keys()]
        df_predictions["%rate"] = [int(key.split('_')[1]) for key in prediction_dict.keys()]
        # Забиваем идеальную нефть и вытаскиваем ближайшего соседа - то есть класс нефти и процент
        # Это обратный подход, то есть мы как будто бы находим на самом деле какой класс и процент использовать,
        # чтобы максимально приблизиться к "Идеальному соотншению парметров в нефти"

        # targets - это слияние класса и процента химии

        # 7,8043, 11,099, 9,2492, 12,641, 8,2895, 835,22, 234,49, 29,635

        X_data = df_predictions.drop(columns=["class", "%rate"])
        y_data = df_predictions[["class", "%rate"]]
        neigh = KNeighborsClassifier(n_neighbors=3)
        neigh.fit(X_data, y_data)
        perfect_petrol = [7.8043, 11.099, 9.2492, 12.641, 8.2895, 835.22, 234.49, 29.635]
        prediction_class_percent = neigh.predict([perfect_petrol])
        df_output.iloc[index, 8] = prediction_class_percent[0][0]
        df_output.iloc[index, 9] = prediction_class_percent[0][1]
    return df_output


@app.post('/upload')
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        buffer = BytesIO(contents)
        df = model_prediction(buffer)
    except:
        raise HTTPException(status_code=500, detail='Что-то пошло не так')
    finally:
        buffer.close()
        file.file.close()
    headers = {'Content-Disposition': 'attachment; filename="predicted_chem.csv"'}
    path = "output_results/predicted_chem.xlsx"
    df.to_excel(path)

    from deep_translator import GoogleTranslator
    english_cols = [GoogleTranslator(source='auto', target='en').translate(word) for word in df.columns]
    df.columns = english_cols
    return Response(df.to_csv(), headers=headers, media_type='text/csv')


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})
