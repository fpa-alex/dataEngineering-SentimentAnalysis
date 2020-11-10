# dataEngineering-SentimentAnalysis

To run our docker program execute :

>docker build -t "webinterface" .
>docker run -p 5000:5000 webinterface

With docker-compose execute:

>docker-compose build
>docker-compose build


You can access the app throught your web browser with :
127.0.0.1:5000 or 0.0.0.0:5000

To run the tests execute :

>python test_app.py
>python test_app_automated.py (after launching docker image)
>pytest test_app1.py
