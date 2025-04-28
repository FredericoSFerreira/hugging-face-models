import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

modelo = "facebook/bart-large-cnn"
url = f"https://api-inference.huggingface.co/models/{modelo}"

reviews = [
    "Comprei essa Smart TV de 60 e estou impressionado com a nitidez e o brilho. Os filmes parecem cinema em casa! A integração com os apps de streaming é perfeita.",
    "Áudio potente, sistema rápido e visual elegante. Fácil de instalar e configurar. Amei o espelhamento com o celular!",
    "Uso com meu PS5 e o desempenho é sensacional. Baixo input lag e suporte a 4K HDR. Só não dei 5 estrelas porque o controle poderia ter teclas iluminadas.",
    "A imagem é boa, o tamanho impressiona, mas o sistema operacional é meio travado às vezes. Demora um pouco para abrir apps como Netflix e YouTube.",
    "Entrega o básico bem, mas o controle remoto é simples demais e o som deixa a desejar. Para quem só quer assistir streaming, serve.",
    "TV grande e bonita, mas a loja de aplicativos é limitada. Não encontrei alguns apps que uso com frequência. Esperava mais nesse quesito.",
    "A imagem é linda, mas o sistema trava muito. Já precisei reiniciar várias vezes só pra conseguir abrir o YouTube.",
    "Precisei conectar uma soundbar porque o áudio é bem fraco. Além disso, a conexão Wi-Fi cai com frequência, mesmo com sinal forte.",
    "Com menos de um mês de uso, a TV começou a apresentar linhas na tela. O suporte da marca foi demorado e pouco eficaz.",
    "A TV parece boa nas especificações, mas o sistema é lento, trava e o controle remoto parou de funcionar em menos de uma semana."
]

payload = {
    'inputs': "\n".join(reviews),
    'options': {'use_cache': False, 'wait_for_model': True},
    "parameters": {
        "min_length": 30,
        "max_length": 180
    }
}

headers = {
    "Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_KEY')}"
}


response = requests.post(url, headers=headers, json=payload, verify=False)
print(response.json())
