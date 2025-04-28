import os

import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/pierreguillou/bert-base-cased-squad-v1.1-portuguese"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_KEY')}"
}

data = {
    "context": "A TV possui uma ótima imagem com suporte a 4K HDR e uma qualidade de som muito boa. O sistema operacional é fluído e não apresenta travamentos.",
    "question": "Qual a qualidade do som da TV?"
}

response = requests.post(API_URL, headers=headers, json=data)
print(response.json())
