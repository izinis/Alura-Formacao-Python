

class Conta: #definindo uma classe

    def __init__(self, numero, titular, saldo, limite): #init é a função construtura que é chamada para construir o objeto
        print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


