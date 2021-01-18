import requests
# Requisição web é você entrar no site.
# Antes de acessar o site, o navegador envia um request (requisição/solicitação) ao servidor que contém o conteúdo do site.
# E por sua vez, o servidor envia um response (resposta) para o navegador.

# Existem os seguintes métodos HTTP para fazer request:
# -> GET: pega informações.
# -> POST: envia informações.
# -> PUT:
# -> DELETE
# -> UPDATE

# requisicao = requests.get('https://putsreq.com/NokF1KefevqiLcXlkfnP')
# print(requisicao)
# print(type(requisicao))
# print(requisicao.status_code)
#print(requisicao.text)

cabecalho = {'User-agent': 'Windows 99'}
requisicao = requests.post('https://putsreq.com/4NAsGClnUUiqR5IEI5Pd', headers=cabecalho)
print(requisicao.status_code)
