# Projete um conjunto de classes para calcular a área e o perímetro de diferentes figuras geométricas, como círculos, retângulos e 
# triângulos. Certifique-se de aplicar o princípio DRY, evitando a repetição de códigos relacionados ao cálculo de áreas e perímetros.

from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

class Retangulo(FiguraGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

circulo = Circulo(raio=5)
retangulo = Retangulo(largura=4, altura=6)
triangulo = Triangulo(base=3, altura=4, lado1=3, lado2=4, lado3=5)

print(f'Área do círculo: {circulo.calcular_area():.2f}')
print(f'Perímetro do círculo: {circulo.calcular_perimetro():.2f}')

print(f'Área do retângulo: {retangulo.calcular_area()}')
print(f'Perímetro do retângulo: {retangulo.calcular_perimetro()}')

print(f'Área do triângulo: {triangulo.calcular_area()}')
print(f'Perímetro do triângulo: {triangulo.calcular_perimetro()}')
