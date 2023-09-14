import requests
import logging

logging.basicConfig(level=logging.INFO)

endpoint = "http://localhost:8000/api/products/"
response = requests.get(endpoint)

logging.info(response)
logging.info(response.json())