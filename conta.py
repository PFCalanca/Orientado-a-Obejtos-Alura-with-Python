
class Conta :

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(" {} possui {} R$ em sua conta.".format(self.titular, self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor



conta = Conta(15700,"Pablito", 5000.00, 10000.00)
conta2 = Conta(19700,"Jurema", 9000.00, 10000.00)
conta3 = Conta(18700,"Lisa", 974.00, 10000.00)

conta3.sacar(200)
conta3.extrato()
