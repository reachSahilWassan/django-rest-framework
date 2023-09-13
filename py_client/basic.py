import logging
import requests

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(filemode="a", filename="api_call_logs", level=logging.INFO)  # save logs to a file

endpoint = "http://localhost:8000/api"

response = requests.get(endpoint)

logging.info(response.status_code)
logging.info(response.json())
