import requests
import logging

logging.basicConfig(level=logging.INFO)
endpoint = "http://localhost:8000/api/products/9/delete/"

response = requests.delete(endpoint, json={"title": "new updated title for test"})

logging.info(response)
# logging.info(response.json())