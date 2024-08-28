#  Dada uma lista de números, escreva uma função que filtre declarativamente apenas os números pares e retorne a lista resultante.

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

numeros = []

while True:
    num = int(input('Digite um número: (Digite um número negativo para sair) '))
    if num < 0:
        break
    numeros.append(num)

pares = filtrar_pares(numeros)
print('Números pares digitados: ',pares)
