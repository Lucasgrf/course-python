#Escreva um programa que conte o número de vogais de uma palavra digitada pelo usuário. 
# Ele usa um loop for para iterar cada caractere da palavra.

palavra = input("Digite uma palavra: ")
vogais = 'aeiou'
contador = 0
for letra in palavra:
    if letra in vogais:
        contador += 1
print("A palavra", palavra, "contém", contador, "vogais.")