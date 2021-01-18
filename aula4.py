convidados = ["Robson", "Kennedy", "Rodrigo", "Manoel"]

print(len(convidados)) # 4
# Estrutura de repetição
print("Estrutura de repetição")
for nome in convidados:
    print(nome)


texto = "Olá mundo"
for letra in texto:
    print(letra)


# Estrutura de laço
print("Estrutura de laço")
numero = 0
while numero <= 5:
    print(f"Número: {numero}")
    numero = numero + 1

# numero = 0 #0
# numero = numero + 1 # 0+1 = 1
# numero = numero + 1 #1+1 = 2
# numero = numero + 1 #2+1 = 3

indice = 0
while indice <= (len(convidados)-1):
    print(convidados[indice])
    indice += 1 # indice = indice + 1

contador = 0
while True:
    print(contador)
    if contador == 5:
        break
    contador += 1
    print("Adicionando mais 1 no contador!!")

print()
num = [1, 2, 3, 4, 5]
i = len(num) #5
while i > 0:
    i -= 1
    if num[i]%2 == 0:
        continue
    else:
        print(num[i])
