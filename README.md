<h1 align="center"><Petrol prediction></h1>

<p align="center"><project-description></p>

## Screenshots

![Home Page](/static/images/preview.jpg "Home Page")

![](/screenshots/2.png)

## Project structure

Folders:

### `Dataset:`,

The app is built using `create-react-app` so this command Runs the app in Development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser. You also need to run the server file as well to completely run the app. The page will reload if you make edits.
You will also see any lint errors in the console.

### `"npm run build": "react-scripts build"`,

Builds the app for production to the `build` folder. It correctly bundles React in production mode and optimizes the build for the best performance. The build is minified and the filenames include the hashes. Your app will be ready to deploy!

### `"npm run test": "react-scripts test"`,

Launches the test runner in the interactive watch mode.

### `"npm run dev": "concurrently "nodemon server" "npm run start"`,

For running the server and app together I am using concurrently this helps a lot in the MERN application as it runs both the server (client and server) concurrently. So you can work on them both together.

### `"serve": "node server"`

For running the server file on you can use this command.

### `npm run serve`

## Built With

- Python
- FastAPI
- env: anaconda with Tensorflow-gpu
- jinja2
- notebooks.ipynb
- CSS,HTML

## Future Updates

- [ ] ML model optimization - MLOps
- [ ] New relevant data from other sources
- [ ] Scaling the dataset into more features
- [ ] Switch to new interface and more functionality
- [ ] Deployment 


## Author

**Ruslan Safaev, Ilsur Yaleev, Alexander Zubov**
telegram links:
- [Ruslan Safaev](https://t.me/MabelHUGO)
- [Ilsur Yaleev]( https://t.me/i_yaleev)
- [Alexander Zubov](https://t.me/dump5)

# Project Description
 ## ПРЕДСКАЗАТЕЛЬНАЯ МОДЕЛЬ ПО ПОДБОРУ ИНДИВИДУАЛЬНОЙ ХИМИИ НА ОСНОВЕ ИИ
 проект создан для : нефтегазовых , нефтехимических и сервесных компаний
 ## ЦЕЛЬ 
 создать алгоритм искусственного интеллекта позволяющий более качественно и быстро проводить лабораторные исследования по подбору химии на проблемные скважины
 ## ПРОЦЕСС МОДЕЛИРОВАНИЯ 
 - Собрана и очищена база данных по нефти и химии , до и после применения       
 - Посчитаны погрешности применения в пласте и в лабораторных условиях       
 - Посчитана эффективность влияния активного вещества , количества вещества в смеси           
 - Подобрана ML                                            
 - Проведены тестовые испытания и добавлены дополительные характеристики для повешения точности         
 ## РЕЗУЛЬТАТЫ ПРОЕКТА
 - Создана уникальная тренировочная БД по нефти и Химии      
 - Создан алгоритм ИИ решающий вышепоставленные задачи        
 - Взаимодействия с потенциальными заказчиками на конференциях ( предложение о коллабе на CollabDay от ПАО Татнефть )    
 - Заявка проекта на финансирование за счёт грантовых средств     
 ## ИСПОЛЬЗОВАНИЕ
 На данный момент проект можно использовать как код для расчетов и подборов химии на основе своих БД    
  P.s на данный момент мы ведём работу над софтом , для адаптация  ее под нужды потребителей , которым планируем сдавать в лизинг
 ## Дальнейшие планы        
 - Подбор дополнительных фичей совместно с экспертами в облисти химии нефти и газа           
 - Разработка софта , в котором будет размещено стартовое решение , также дополнительно туда будут добавляться НИОКРЫ и стартапы на основе ИИ , которые потребитель также сможет использовать 
