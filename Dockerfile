FROM python:3

WORKDIR /app

ENV FLASK_APP=app.py

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./webinterface/app.py .
COPY ./webinterface/templates/ ./templates/
COPY ./model-learning/vectorizer.pkl .
COPY ./model-learning/sentiment_classifier.pkl .

RUN ls -lrt

EXPOSE 5000

CMD ["python", "app.py"]