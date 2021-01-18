'''
Exercício: Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número
dentro dessa coleção. Faça outra função que retorna o menor número dessa coleção.
'''

# def maior_numero(lista_numero):
#     return max(lista_numero)
#
# def menor_numero(lista_numero):
#     return min(lista_numero)

def maior_numero(lista_numero):
# [55,5,93,0]
# 55>0 #55
# 55>93 #93
# 93>5 #93
    numeros = lista_numero
    maior = numeros[0]
    contador = len(numeros)-1 #3
    while contador > 0:
        if maior > numeros[contador]:
            maior = maior
        else:
            maior = numeros[contador]
        contador -= 1

    return maior

def menor_numero(lista_numero):
# [55,5,93,0]
# 55<5 #5
# 5<93 #5
# 5<0 #0
    numeros = lista_numero
    menor = numeros[0]
    contador = len(numeros)-1 #3
    while contador > 0:
        if menor < numeros[contador]:
            menor = menor
        else:
            menor = numeros[contador]
        contador -= 1

    return menor


numeros = [55,5,93,0]

print(f"O maior número da lista {numeros} é {maior_numero(numeros)}")
print(f"O menor número da lista {numeros} é {menor_numero(numeros)}")
