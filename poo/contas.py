from clientes import Clientes

class Contas(Clientes): #molde para criar objetos do tipo conta

    def __init__(self, nome, sobrenome, cpf, idade):
        super(Contas, self).__init__(nome, sobrenome, cpf, idade)
        self.saldo = 0

    def __repr__(self):
        return f"A conta de {self.nome} {self.sobrenome} foi criada com sucesso!"

    def consultar_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if valor <= self.consultar_saldo():
            self.saldo -= valor
            return f"O saque de {valor}$ foi realizado com sucesso!"
        else:
            return "Não foi possível realizar a operação. Pois, o seu saldo é insuficiente!"

    def depositar(self, valor):
        if valor >= 5:
            self.saldo += valor
            return "A operação foi realizada com sucesso!"
        else:
            return "Não foi possível realizar a operação. Pois, o valor mínimo para depositar é 5$"
