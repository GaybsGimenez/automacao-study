import requests


url = "https://www.google.com.br"
response = requests.get(url)
print(response)
print(response.text)
# print(response.content)
#print(response.json)



with open("files/page.html", "w") as page:
    page.write(response.text)