import os

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from dotenv import load_dotenv

load_dotenv()
API_URL = "https://api-inference.huggingface.co/models/neuralmind/bert-base-portuguese-cased"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_KEY')}"
}

data = {
    "inputs": "Essa TV tem uma qualidade de [MASK] incrível"
}

response = requests.post(API_URL, headers=headers, json=data)
results = response.json()
for result in results:
    print(result)
