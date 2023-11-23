class Conta: #criação da classe conta
    def __init__(self, titular, nConta, saldo, chequeEsp): #definição das propriedades/atributos da classe
        self.titular = titular
        self.nConta = nConta
        self.saldo = saldo
        self.chequeEsp = chequeEsp

    def consultar(self): #criação de método a ser aplicado em classe
        print(f'Titular: {self.titular}')
        print(f'Saldo: {self.saldo}')
        print('-' *30)

    def depositar(self, valor): #criação de método a ser aplicado em classe
        self.saldo += valor

    def sacar(self, valor): #criação de método a ser aplicado em classe
        if self.saldo >= valor:
            self.saldo -= valor
        elif self.chequeEsp:
            print(f'Podemos conceder {valor - self.saldo} reais a você por ser nosso cliente especial!')
            self.saldo -= valor
        else:
            print('Saldo Insuficiente')

    def transferir(self, valor, cDestino):
        if self.saldo >= valor :
            self.saldo -= valor
            cDestino.depositar(valor) # cDestino.saldo += valor
        else:
            print('Saldo Insuficiente')


c1 = Conta('Cintia', 100, 1000, True)
c2 = Conta('Juli', 201, 0, False)

# chamando funções
c1.transferir(3000, c2)
c2.consultar()
#c1.sacar(2000)
#c1.consultar()
#c1.depositar(500)
#c1.consultar()

