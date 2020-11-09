import unittest
import app

class TestAPP(unittest.TestCase):

	def test_machineLearningPrediction(self):
		self.assertEqual(app.machineLearningPrediction(" I'd have responded, if I were going"),{'Prediction' : 'neutral'})
		self.assertNotEqual(app.machineLearningPrediction(" I'd have responded, if I were going"),{'Prediction' : 'negative'})
		self.assertNotEqual(app.machineLearningPrediction(" I'd have responded, if I were going"),{'Prediction' : 'positive'})
		
	
if __name__ == '__main__':
	unittest.main()