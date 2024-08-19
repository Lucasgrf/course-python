# Desenvolva um programa que converta uma quantia de dinheiro de dólares em euros. 
# Solicite ao usuário o valor em dólares e a taxa de câmbio atual.
dolar = float(input("Insira o valor em dólares: "))
taxa = float(input("Insira a taxa de câmbio atual: "))
euro = dolar * taxa
print(f"O valor em euros é € {euro:.2f}.")