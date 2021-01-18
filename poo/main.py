# Orientação a Objeto
from contas import Contas

conta = Contas("Robson", "Daniel", "012.456.256-89", 28)
print(conta)
print(f"Olá {conta.nome} {conta.sobrenome}.")
print(f"O saldo da sua conta é: {conta.consultar_saldo()}$")
print(conta.sacar(10))

print(conta.depositar(5))
print(f"O saldo da sua conta é: {conta.consultar_saldo()}$")
print(conta.sacar(3))
print(f"O saldo da sua conta é: {conta.consultar_saldo()}$")
