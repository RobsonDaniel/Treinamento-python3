# Passagem de argumentos

#biblioteca (função)
import sys

argumentos = sys.argv # retorna uma lista de string onde o primeiro item dessa lista é o nome do arquivo

def soma(n1, n2):
    return float(n1)+float(n2)

def multiplicar(n1, n2):
    return float(n1)*float(n2)

if len(argumentos) == 4:
    if argumentos[1] == 'soma':
        print(soma(argumentos[2], argumentos[3]))
    elif argumentos[1] == 'multiplicar':
        print(multiplicar(argumentos[2], argumentos[3]))
    else:
        print("Opção invalida!")
else:
    print("É necessário passar três argumentos!")
