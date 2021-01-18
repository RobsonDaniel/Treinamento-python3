'''
Exercício: Faça um programa que leia a quantidade de pessoas que serão convidados
para uma festa. Após isso o programa irá perguntar o nome de todas as pessoas e
colocar em uma lista de convidados e imprimir todos os nomes da lista.
'''

convidados = []
qt_pessoas = int(input("Digite a quantidade de pessoas que serão convidados para a festa: "))

contador = 0
while contador < qt_pessoas:
    convidado = input("Digite o nome do convidado: ")
    convidados.append(convidado)
    contador += 1

for convidado in convidados:
    print(convidado)
