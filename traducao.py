from transformers import pipeline
from dotenv import load_dotenv
import urllib3

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

pipe = pipeline("translation", model="facebook/mbart-large-50-many-to-many-mmt", src_lang='pt_XX', tgt_lang='en_XX')

translate = pipe('Olá, eu gosto de utilizar inteligência artificial.')

print(translate)
