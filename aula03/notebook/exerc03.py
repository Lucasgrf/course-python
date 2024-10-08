#Modele um Objeto Conta Bancária, para o qual crie uma classe com os seguintes atributos: 
# titular da conta, saldo em sua conta bancária e o tipo de conta além do tipo de moeda da conta (dólar ou moeda nacional). 
# Atributos como saldo serão, por exemplo, do tipo decimal, e o tipo de conta será do tipo string, então o titular será do tipo pessoa, 
# para isso também precisamos modelar esse objeto (criar a classe Pessoa com os atributos Nome, Identificação, Nacionalidade) 
# portanto o titular será do tipo Pessoa.

#Atividades:
#Crie a classe Conta Bancária
#Crie a classe Pessoa
#Crie uma instância da classe Pessoa usando o construtor
#Crie uma instância da classe Conta usando o construtor, lembre-se que o atributo titular é do tipo pessoa então 
# a instância criada do tipo pessoa deve ser atribuída a ele.

class Pessoa:
    def __init__(self, nome, identificacao, nacionalidade):
        self.nome = nome
        self.id = identificacao
        self.nacionalidade = nacionalidade

    def __str__(self):
        return f"{self.nome} ({self.nacionalidade})"

class Conta:
    def __init__(self, titular: Pessoa, saldo: float, tipo_conta: str, moeda: str):
        self.titular = titular
        self.saldo = saldo
        self.tipo_conta = tipo_conta
        self.moeda = moeda

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso.")
        else:
            print("Saldo insuficiente ou valor de transferência inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual: {self.moeda} {self.saldo:.2f}")

    def consultar_titular(self):
        print(f"Titular da conta: {self.titular}")

    def consultar_tipo_conta(self):
        print(f"Tipo de conta: {self.tipo_conta}")

    def consultar_moeda(self):
        print(f"Moeda: {self.moeda}")


pessoa1 = Pessoa("João", "123456789", "Brasileiro")
conta1 = Conta(pessoa1, 1000.0, "Corrente", "Real")


conta1.consultar_titular()
conta1.consultar_moeda()
conta1.consultar_saldo()
conta1.consultar_tipo_conta()
