#Desenvolva um programa que solicite ao usuário que insira os comprimentos dos dois catetos de um 
# triângulo retângulo e calcule o comprimento da hipotenusa.

import math

cateto1 = float(input("Insira o comprimento do primeiro cateto: "))
cateto2 = float(input("Insira o comprimento do segundo cateto: "))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print(f"O comprimento da hipotenusa é {hipotenusa:.2f}.")