# dataEngineering-SentimentAnalysis

To run our docker program manualy execute :

>docker build -t "webinterface" .
>docker run -p 5000:5000 webinterface

With docker-compose execute:

>docker-compose up


You can access the app throught your web browser with :
127.0.0.1:5000 (Windows) or 0.0.0.0:5000 (Linux)

To run the tests execute :

>python test_app.py
>python test_app_automated.py (after launching docker image)
>pytest test_app1.py
