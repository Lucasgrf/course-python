#Temos a imagem a seguir mostrando os diferentes carros que uma loja online possui, 
# defina através de abstração quais atributos e quais métodos o objeto carro_brinquedo deve 
# ter que sejam relevantes para criar a classe de acordo com o contexto da loja online

#Atividades a serem realizadas:

#Criar a classe com os atributos e métodos relevantes através da abstração e contexto de uma loja online
#Utilize o construtor para criar instâncias da classe CarroBrinquedo

class CarroBrinquedo:
    def __init__ (self,fabricante,marca,cor,modelo,tamanho,ligado_desligado,bateria,preco, dimensoes: dict):
        self.fabricante = fabricante
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.tamanho = tamanho
        self.estado = ligado_desligado
        self.bateria = bateria
        self.preco = preco
        self.dimensoes = dimensoes
        
    def __str__(self):
        return f"Fabricante: {self.fabricante}\nMarca: {self.marca}\nCor: {self.cor}\nModelo: {self.modelo}\nTamanho: {self.tamanho}\nEstado: {self.estado}\nBateria: {self.bateria}\nPreço: {self.preco}\nDimensões: {self.dimensoes}"
    
    def andar_frente(self):
        if(self.estado):
            if(self.bateria >= 10):
                self.bateria -= 10
                print("Andando em frente.")
            else:
                print("Descarregado!")
        else:
            print("Ligue o carrinho para executar o comando.")

    def andar_tras(self):
        if(self.estado):
            if(self.bateria >= 10):
                self.bateria -= 10
                print("Andando para trás.")
            else:
                print("Descarregado!")
        else:
            print("Ligue o carrinho para executar o comando.")

    def andar_esquerda(self):
        if(self.estado):
            if(self.bateria >= 10):
                self.bateria -= 10
                print("Andando para a esquerda.")
            else:
                print("Descarregado!")
        else:
            print("Ligue o carrinho para executar o comando.")

    def andar_direita(self):
        if(self.estado):
            if(self.bateria >= 10):
                self.bateria -= 10
                print("Andando para a direita.")
            else:
                print("Descarregado!")
        else:
            print("Ligue o carrinho para executar o comando.")

    def freiar(self):
        if(self.estado):
            self.bateria -= 10
            print("Freiando.")
        else:
            print("Ligue o carrinho para executar o comando.")

    def acelerar(self):
        if(self.estado):
            if(self.bateria >= 10):
              self.bateria -= 10
              print("Acelerando.")
            else:
                print("Descarregado!")
        else:
            print("Ligue o carrinho para executar o comando.")

    def ligar(self):
        if not self.estado:
            self.estado = True
        if(self.bateria > 0):
            print("Carrinho ligado.")
        else:
            print("Carrinho sem bateria suficiente. Recarregue!")

    def desligar(self):
        if(self.estado):
            self.estado = False
            print("Carrinho desligado.")

    def nivelBateria(self):
        if(self.bateria >= 75):
            print(f"Bateria não precisa de carga! Quantidade atual: {self.bateria}%")
        elif(self.bateria >= 50):
            print(f"Bateria na metade da carga! Quantidade atual: {self.bateria}%")
        elif(self.bateria >= 10):
            print(f"Bateria precisa de uma recarga! Quantidade atual: {self.bateria}%")

my_car = CarroBrinquedo("Candide","Candide","Vermelho","Fusca", "Pequeno", False, 100, 100, {"Altura": 10, "Largura": 5, "Comprimento": 10})

print(my_car)
