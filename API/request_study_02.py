import requests

# metodo get
# url = "https://httpbin.org/get"

# response = requests.get(url)
# print(response)
# print(response.text)

#_________________________________________________

# metodo post
url = "https://httpbin.org/post"
data = {
    "pessoa" : {
        "nome": "Rodrigo",
        "profissao": "professor"
    }
    
}

params = {
    "dataIni": "2025-01-01",
    "dataFim": "2025-12-31"
}

response = requests.post(url, json=data, params=params)
print(response)
print(response.request.url)
print(response.text)