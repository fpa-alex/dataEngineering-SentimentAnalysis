from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


with open('vectorizer.pkl', 'rb') as f:
	vectorizer = pickle.load(f)

with open('sentiment_classifier.pkl','rb') as f:
	sentiment_classifier = pickle.load(f)
	

def machineLearningPrediction(phrase):
	print("## Phrase : "+ phrase+" ##")
	user_input = vectorizer.transform([str(phrase)])
	prediction = sentiment_classifier.predict(user_input)
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')