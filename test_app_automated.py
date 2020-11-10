import unittest
import os
import requests
from flask import Flask, request, render_template

class FlaskTests(unittest.TestCase):

	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		self.parameters = {
			'phrase_neutral': " I'd have responded, if I were going"
		}
		pass
	
	def teardDown(self):
		pass
		
	def test_machineLearningPrediction(self):
	
		params = {
			'phrase': self.parameters['phrase_neutral']
		}		
		response = requests.post('http://localhost:5000', data=params)
		self.assertEqual(response.status_code, 200)
		self.assertFalse(response.text.find("neutral")== -1)
		self.assertTrue(response.text.find("negative"), -1)
		self.assertTrue(response.text.find("positive"), -1)

if __name__ == '__main__':
	unittest.main()