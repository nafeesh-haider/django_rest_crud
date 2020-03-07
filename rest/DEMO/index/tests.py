from django.test import TestCase
import requests


def test_api(request):
	headers = {
	    'Content-Type': 'application/json',
	}

	data = '{"username": "HADES666","password": "ispl123;"}'

	response = requests.post('http://127.0.0.1:8000/api/auth/token/login/', headers=headers, data=data)

	print(response.text, '<<<<,,')

# Create your tests here.
