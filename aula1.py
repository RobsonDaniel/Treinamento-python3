# comentário de uma linha
'''
Comentário
de várias
linhas
'''

"""
Comentário de
várias linhas
"""

print("Hello World!")
print('Hello World!')

print("Nova\nlinha")

print("tabe\tpara\tcriar\tcoluna")

nome = "Robson"
sobrenome = "Daniel"
idade = 24
peso = 68.80

print(nome)
print("O seu nome é", nome, sobrenome, "e tem", idade, "anos.")
print("O seu nome é " + nome + " " + sobrenome + " e tem " + str(idade) + " anos.")
print(f"{nome} {sobrenome}")
print(f"tipo da variável: {type(nome)}")
print(f"tipo da variável: {type(idade)}")
print(f"tipo da variável: {type(peso)}")

usuario = input("Digite o seu nome: ")
print(f"Olá {usuario}.")
print(f"tipo da variável: {type(usuario)}")

numero1 = 10
numero2 = 58

print(numero1+numero2)
print(numero1-numero2)
print(numero1/numero2)
print(numero1**numero1)
