# https://www.w3schools.com/python/python_regex.asp
# Python RegEx
# Um RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
# RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado.

# Importando o remódulo
# Python tem um pacote embutido chamado re, que pode ser usado para trabalhar com expressões regulares.
import re # Módulo RegEx

# Funções RegEx
# O remódulo oferece um conjunto de funções que nos permite pesquisar uma string para uma correspondência:
# Função        Descrição
# findall       Retorna uma lista contendo todas as correspondências
# search        Retorna um objeto Match se houver uma correspondência em qualquer lugar da string
# split         Retorna uma lista onde a string foi dividida em cada partida
# sub           Substitui uma ou mais correspondências por uma string

# METACARACTERES
# Metacaracteres são caracteres com um significado especial:

# METACARACTERES   DESCRIÇÃO
#       []         define um conjunto de caracteres.
a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
b = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
print(re.findall(r'[abc]', a)) # ['a', 'b', 'c']
print(re.findall(r'[a-c]', a)) # ['a', 'b', 'c']
print(re.findall(r'[a-c]', b)) # []
print(re.findall(r'[A-C]', b)) # ['A', 'B', 'C']
print(re.findall(r'[F-P]', b)) # ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

c = '0 1 2 3 4 5 6 7 8 9 10 11 12'
print(re.findall(r'[0-9]', c)) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '0', '1', '1', '1', '2']
print(re.findall(r'[0-9]', c))

d = 'O rato roeu a ropa do rei de roma!'
print(re.findall(r'ropa', d)) # ['ropa']
print(re.findall(r'r\w', d)) # ['ra', 'ro', 'ro', 're', 'ro']
print(re.findall(r'ro\w+', d)) # ['roeu', 'ropa', 'roma']


#       \          Sinaliza uma sequência especial (também pode ser usado para escapar de caracteres especiais)
#       []
#       []
