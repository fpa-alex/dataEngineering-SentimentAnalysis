from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


with open('../model-learning/vectorizer.pkl', 'rb') as f:
	vectorizer = pickle.load(f)

with open('../model-learning/sentiment_classifier.pkl','rb') as f:
	sentiment_classifier = pickle.load(f)
	

def machineLearningPrediction(phrase):
	print("## Phrase : "+ phrase+" ##")
	user_input = vectorizer.transform([str(phrase)])
	prediction = sentiment_classifier.predict(user_input)
	#result = lambda x: 'Negative' if prediction == 0 else ('Neutral' if prediction == 1 else 'Positive') 
	output = {'Prediction': prediction[0]}
	return output

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' :
        details = request.form
        result = machineLearningPrediction(details['phrase'])
        return render_template('index.html', result=result)
        
    else :
        return render_template('index.html')

if __name__ == 'main':
    app.run(host='0.0.0.0')

