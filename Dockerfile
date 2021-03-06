FROM python:3

WORKDIR /app

ENV FLASK_APP=app.py

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app.py .
COPY ./templates/ ./templates/
COPY ./vectorizer.pkl .
COPY ./sentiment_classifier.pkl .

RUN ls -lrt

EXPOSE 5000

CMD ["python", "app.py"]