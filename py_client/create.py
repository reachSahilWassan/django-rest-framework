import requests
import logging

logging.basicConfig(level=logging.INFO)

endpoint = "http://localhost:8000/api/products/"
data = {"title": "This field is done", "price": 99.93}
response = requests.post(endpoint, json=data)

logging.info(response)
logging.info(response.json())