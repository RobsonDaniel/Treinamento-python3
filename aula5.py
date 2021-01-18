# Estrutura de dados

# Lista ([])
frutas = ['Abacaxi', 'Uva', 'Melancia', 'Banana']

print(frutas[0])

for fruta in frutas:
    print(fruta)

if 'Abacaxi' in frutas:
    print("A fruta Abacaxi existe na lista de fruta!")

# Tupla (()) é igual a uma lista. Porém, não é possível adicionar ou remover, ou seja é inalterável.
usuario_senha = ('robinho', 15289)
print(usuario_senha)

print(usuario_senha[0])

for dados in usuario_senha:
    print(dados)

# Dicionário ({})
pessoa = {'nome': 'Robson', 'sobrenome': 'Daniel', 'idade': 24, 'peso': 60, }

pessoa['telefone'] = '868686868'

print(pessoa)

print(pessoa['nome'])

for chave in pessoa:
    print(pessoa[chave])

# Conjunto (set()) é igual a uma lista. Porém, não é ordenado e não possui itens repetidos
convidados = {'Robson', 'Daniel', 'Oliveira'}

print(convidados)
convidados.add('Robson')
convidados.add('Kennedy')
print(convidados)

convidados.remove('Oliveira')
print(convidados)
