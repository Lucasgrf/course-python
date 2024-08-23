#Crie um programa no qual o computador escolhe um número aleatório entre 1 e 100 e depois pede ao usuário que adivinhe o número. 
# Fornece pistas que indicam se o número a ser adivinhado é maior ou menor. Use um loop while até que o usuário adivinhe corretamente.

import random

numero = random.randint(1, 100)
tentativa = 0
palpite = 0
print("Tente adivinhar um número entre 1 e 100.")
numero_usuario = int(input("Digite um número: "))
while numero_usuario != numero:
    if numero_usuario < numero:
        print("O número é maior.")
    else:
        print("O número é menor.")
    tentativa += 1
    numero_usuario = int(input("Digite um número entre 1 e 100: "))
    palpite += 1
print("Parabéns! Você adivinhou o número em", tentativa, "tentativas.")
