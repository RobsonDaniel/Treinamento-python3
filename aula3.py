string = 'Hello world!'

print(string[0]) #H
print(string[-1]) #!

print(string[0:5])
print(string[0:-1:2]) #Hlowrd

print(string.lower())
print(string.upper())

print(string.split(" "))

print(f"O número de caracteres do texto é: {len(string)}")

lista = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']

print(f"O número de itens da lista é: {len(lista)}")

print(f"Quantidade de letras l: {lista.count('l')}")

print(lista[0])
print(lista[-1])
print(lista[0:-1])

convidados = ["Robson", "Kennedy", "Rodrigo", "Manoel"]

convidados[0] = "Robson Daniel"
print(convidados)

convidados.append("Arthur")
print(convidados)

convidados.insert(0, "Hudson")
convidados.insert(2, "Filipe")
print(convidados)

convidados.remove("Robson Daniel")
print(convidados)

print(f"O item da lista removido foi: {convidados.pop()}")
print(convidados)
