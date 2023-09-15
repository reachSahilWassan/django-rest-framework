import requests
import logging

logging.basicConfig(level=logging.INFO)

endpoint = "http://localhost:8000/api/products/2/update/"

response = requests.put(endpoint, json={"title": "new updated title for test"})

logging.info(response)
logging.info(response.json())