import requests
import logging

logging.basicConfig(level=logging.INFO)

endpoint = "http://localhost:8000/api/products/2/"

response = requests.get(endpoint, json={"title": "new name"})

logging.info(response)
logging.info(response.json())