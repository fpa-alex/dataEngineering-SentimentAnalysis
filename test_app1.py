import pytest
import app

@pytest.mark.parametrize(
	('input', 'expected'),
	(
		(" I'd have responded, if I were going", {'Prediction' : 'neutral'}),
		("Sooo SAD I will miss you here in San Diego!!!", {'Prediction' : 'negative'}),
		("2am feedings for the baby are fun when he is all smiles and coos", {'Prediction' : 'positive'}),
	)
)

def test_machineLearningPrediction(input, expected):
	assert app.machineLearningPrediction(input) == expected