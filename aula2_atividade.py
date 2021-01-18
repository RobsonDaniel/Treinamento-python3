'''
faça um programa que pergunte a idade, o peso e a altura de uma pessoa
e decida se ela está apta a ser do Exercito.
Para entrar no Exercito é preciso ter mais de 18 anos, pesar mais ou igual a 60
kilos e medir mais ou igual a 1,70 metros.
'''

idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

if idade > 18 and peso >= 60 and altura >= 1.70:
    print("Você está apto a entrar no Exercito!")
else:
    print("Você não está apta a entrar no Exercito!")
