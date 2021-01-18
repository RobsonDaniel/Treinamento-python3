'''
Exercício: faça um formulário que pergunte o
nome, cpf, endereço, idade, altura e telefone
e imprima isso em um relatório organizado
'''

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
altura = input("Digite a sua altura: ")
telefone = input("Digite o seu telefone: ")
cpf = input("Digite o seu cpf: ")
endereco = input("Digite o seu endereço: ")

print("NOME\tIDADE\tALTURA\tTELEFONE\tCPF\tENDEREÇO")
print(f"{nome}\t{idade}\t{altura}\t{telefone}\t{cpf}\t{endereco}")
