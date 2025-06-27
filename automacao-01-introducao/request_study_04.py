import requests
from pprint import pprint



url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/"
params = {
    "view":"nivelado"
}

response = requests.get(url)

try: 
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    result = None
else:
    result = response.json()
    pprint(result)
