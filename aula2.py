# Operadores lógicos
var_verdadeiro = True
var_falso = False

print(var_falso)
print(var_verdadeiro)

# tipo Boolean
print(type(var_falso))
print(type(var_verdadeiro))

print(1>2)
print(1<2)
print(2==2)
print(1!=1)
print(2>=2)
print(2<=3)

print(1>1 and 1==1)
print(1>1 or 1==1)
print(-1>0 or 1<2)

print(not False)
print(not True)

# Estrutura de decisão

#IF
if True:
    print("imprimindo o valor")

if False:
    print("não imprimindo o valor")

if var_verdadeiro == True:
    print("O valor de var_verdadeiro é verdadeiro")

# IF E ELSE
if False:
    print("imprimindo o valor")
else:
    print("não imprimindo o valor")

if True:
    print("imprimindo o valor 1")
if True:
    print("imprimindo o valor 2")
if False:
    print("imprimindo o valor 3")
else:
    print("não imprimindo o valor 4")

if var_falso == True:
    print("O valor de var_verdadeiro é verdadeiro")
else:
    print("O valor de var_falso é falso")

# IF, ELIF E ELSE
if True:
    print("imprimindo o valor do if")
elif True:
    print("imprimindo o valor do elif")
else:
    print("não imprimindo o valor")

if False:
    print("imprimindo o valor do if")
elif True:
    print("imprimindo o valor do elif")
else:
    print("não imprimindo o valor")

if False:
    print("imprimindo o valor do if")
elif False:
    print("imprimindo o valor do elif")
else:
    print("não imprimindo o valor")
