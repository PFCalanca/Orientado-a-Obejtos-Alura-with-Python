
class Conta :

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(" {} possui {} R$ em sua conta.".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O saque de R${} está acima do limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"



conta = Conta(15700,"Pablito", 5000.00, 10000.00)
conta2 = Conta(19700,"Jurema", 9000.00, 10000.00)
conta3 = Conta(18700,"Lisa", 974.00, 10000.00)

conta.extrato()
conta3.extrato()
conta3.transferir(200, conta)
conta.extrato()
conta3.extrato()

print(conta.saldo)

conta3.sacar(500000)

print(Conta.codigo_banco())
