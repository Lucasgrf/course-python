# Alex, Maria e Jonas são objetos do tipo Pessoa que possuem uma infinidade de atributos. 
# Alex precisa fornecer dados para se cadastrar em uma clínica médica, enquanto Maria acredita em esoterismo e 
# está se cadastrando em uma agência esotérica para marcar uma consulta com o vidente. Jonas , por sua vez, 
# está se cadastrando em uma rede social, como vocês podem ver são 3 contextos diferentes. 
# Você será solicitado a modelar os objetos (Alex, Maria e Jonas) em três classes de acordo com o contexto explicado no enunciado, 
# o resultado serão 3 classes e a diferença serão os atributos que você os define através da abstração.
#Você pode adicionar um único método que exiba as informações de cada um desses objetos na tela (alex, maria, jonas)
#Tomemos como exemplo a seguinte imagem explicada em aula, você pode adicionar atributos se achar necessário
#Você deve levar em consideração as seguintes atividades:

#Classe Pessoa modelada a partir do aplicativo de cadastro de uma clínica médica
#Classe Pessoa modelada a partir do aplicativo de registro de um centro esotérico
#Classe Pessoa modelada a partir do aplicativo de cadastro de uma rede social
#Criar instâncias dos 3 objetos do tipo Pessoa (Alex, Maria e Jonas)
#Mostrar as informações dos objetos através do método mostrar informação

def mostrar_informacao(pessoa):
    if pessoa.nome is not None:
        print(f"Nome: {pessoa.nome}")
    if pessoa.idade is not None:
        print(f"Idade: {pessoa.idade}")
    if pessoa.sexo is not None:
        print(f"Sexo: {pessoa.sexo}")
    if pessoa.peso is not None:
        print(f"Peso: {pessoa.peso}")
    if pessoa.signo is not None:
        print(f"Signo: {pessoa.signo}")
    if pessoa.tipoSanguineo is not None:
        print(f"Tipo Sanguíneo: {pessoa.tipoSanguineo}")
    if pessoa.corOlhos is not None:
        print(f"Cor dos Olhos: {pessoa.corOlhos}")
    if pessoa.altura is not None:
        print(f"Altura: {pessoa.altura}")
    if pessoa.hobbies is not None:
        print(f"Hobbies: {pessoa.hobbies}")
    print("\n")


class Pessoa:
    def __init__(self, nome=None, idade=None, sexo=None, peso=None, signo=None, tipoSanguineo=None, corOlhos=None, altura=None, hobbies=None):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.signo = signo
        self.tipoSanguineo = tipoSanguineo
        self.corOlhos = corOlhos
        self.altura = altura
        self.hobbies = hobbies

class App:
    class ClinicaMedica:
        def __init__ (self,pessoa: Pessoa):
            self.nome = pessoa.nome
            self.idade = pessoa.idade
            self.sexo = pessoa.sexo
            self.peso = pessoa.peso
            self.tipoSanguineo = pessoa.tipoSanguineo
            self.altura = pessoa.altura

        def mostrar_informacao(self):
            mostrar_informacao(Pessoa(self.nome, self.idade, self.sexo, self.peso, None, self.tipoSanguineo, None, self.altura, None))
        
    class CentroEsoterico:
        def __init__ (self,pessoa: Pessoa):
            self.nome = pessoa.nome
            self.idade = pessoa.idade
            self.signo = pessoa.signo

        def mostrar_informacao(self):
            mostrar_informacao(Pessoa(self.nome, self.idade, None, None, self.signo, None, None, None, None))

    class RedeSocial:
        def __init__ (self,pessoa: Pessoa):
            self.nome = pessoa.nome
            self.idade = pessoa.idade
            self.sexo = pessoa.sexo
            self.hobbies = pessoa.hobbies
            self.corOlhos = pessoa.corOlhos
            self.altura = pessoa.altura

        def mostrar_informacao(self):
            mostrar_informacao(Pessoa(self.nome, self.idade, self.sexo, None, None, None, self.corOlhos, self.altura, self.hobbies))

AppClinicaMedica = App.ClinicaMedica(Pessoa("Alex", 25, "Masculino", 70, None, "O+", None, 1.75, None)) 
AppCentroEsoterico = App.CentroEsoterico(Pessoa("Maria", 30, "Feminino", None, "Leão", "A+", None, 1.60, None))
AppRedeSocial = App.RedeSocial(Pessoa("Jonas", 20, "Masculino", None, None, None, "Verde", 1.80,"Assistir séries"))

AppClinicaMedica.mostrar_informacao()
AppCentroEsoterico.mostrar_informacao()
AppRedeSocial.mostrar_informacao()
