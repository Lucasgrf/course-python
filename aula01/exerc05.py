#Escreva um programa que solicite ao usuário o peso (em quilogramas) e a altura (em metros) e calcule o IMC.

peso = float(input("Insira o seu peso em quilogramas: "))
altura = float(input("Insira a sua altura em metros: "))

IMC = peso / (altura ** 2)

print(f"O seu IMC é {IMC:.2f}.")