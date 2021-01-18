# Entrada e saída de arquivos

america_latina = [
    'Brasil',
    'Argentina',
    'Uruguai',
    'Paraguai',
    'Chile',
    'Peru',
    'Colombia',
    'Venezuela',
    'Bolivia',
    'Equador'
]

arquivo = open('aula8_arquivo.txt', 'a', encoding='UTF-8') # nome do arquivo, modo de abertura do arquivo
print(arquivo)
for pais in america_latina:
    arquivo.write(pais+'\n')

print(f"O arquivo {arquivo.name} foi criado!")
arquivo.close()

ler_arq = open(arquivo.name, 'r', encoding='UTF-8')
print(ler_arq)
print(f"Países:\n{ler_arq.read()}")
ler_arq.close()

def ler(txt):
    with open(txt.name, 'r', encoding='UTF-8') as arquivo:
        print(f"Países:\n{arquivo.read()}")

ler(ler_arq)
