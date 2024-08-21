# Crie um programa que determine o tipo de triângulo (equilátero, isósceles ou escaleno) com base no comprimento de seus lados.

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if(lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1):
    print("Não é um triângulo")
elif(lado1 == lado2 and lado2 == lado3):
    print("Triângulo equilátero")
elif(lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")