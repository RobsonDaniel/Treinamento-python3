def divisao(n1, n2):
    return n1/n2

try:
    print(divisao(1, 0))
except Exception as e:
    print(f"Erro: {e}")
