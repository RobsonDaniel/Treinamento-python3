import requests
import json
#http://www.omdbapi.com/
# https://viacep.com.br/

cep = int(input("Digite o seu CEP (apenas número): "))

def api_buscar_endereco(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    return requests.get(url)

def pesquisa(dados):
    if dados.status_code == 200:
        endereco = json.loads(dados.text)
        print("\nEndereço encontrado:")
        print(f"UF: {endereco['uf']}")
        print(f"Cidade: {endereco['localidade']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Nome da rua: {endereco['logradouro']}")
    else:
        print("Não foi possível encontrar o endereço pelo cep.")


pesquisa(api_buscar_endereco(cep))
