import unittest
import app

class TestAPP(unittest.TestCase):

	def test_machineLearningPrediction_neutral(self):
		self.assertEqual(app.machineLearningPrediction(" I'd have responded, if I were going"),{'Prediction' : 'neutral'})
		
	def test_machineLearningPrediction_negative(self):
		self.assertEqual(app.machineLearningPrediction("Sooo SAD I will miss you here in San Diego!!!"),{'Prediction' : 'negative'})
		
	def test_machineLearningPrediction_positive(self):
		self.assertEqual(app.machineLearningPrediction("2am feedings for the baby are fun when he is all smiles and coos"),{'Prediction' : 'positive'})
		
	
if __name__ == '__main__':
	unittest.main()