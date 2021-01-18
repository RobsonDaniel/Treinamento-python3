import requests
import json

request = requests.get("https://economia.awesomeapi.com.br/json/all")

cotacao = json.loads(request.text)
#print(cotacao['USD'])

dolar = f"O {cotacao['USD']['name']} está custando {cotacao['USD']['high']} reais."
print(dolar)
