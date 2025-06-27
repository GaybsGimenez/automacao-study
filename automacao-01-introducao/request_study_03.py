import requests
from pprint import pprint

name = input("Digite um nome para a pesquisa:\n ")

url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"

params = {
    "localidade":33 #RJ
}

response = requests.get(url, params=params)

try: 
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    result = None
else:
    result = response.json()
    pprint(result)
