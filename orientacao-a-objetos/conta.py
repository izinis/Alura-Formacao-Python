

class Conta: #definindo uma classe

    def __init__(self, numero, titular, saldo, limite): #init é a função construtura que é chamada para construir o objeto
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do títular {}". format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def pega_saldo(self):
        return self.__saldo

    def devolve_titular(self):
        return self.__titular

    def retorna_limite(self):
        return self.__limite

