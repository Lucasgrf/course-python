#Implemente um programa que calcule o desconto aplicado em uma compra, considerando as seguintes regras:

#Se o valor da compra for maior ou igual a $100, será aplicado um desconto de 10%.
#Se o valor da compra for maior ou igual a $200, será aplicado um desconto de 20%.

valor_compra = float(input("Digite o valor da compra: "))
desconto = 0
if(valor_compra >= 100):
    desconto = 0.1
elif(valor_compra >= 200):
    desconto = 0.2
    
valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

if(desconto == 0):
    print(f"Valor total: {valor_final}")
elif(desconto > 0):
    print(f"Valor do desconto: {valor_desconto:.2f}")
    print(f"Valor total com desconto: {valor_final:.2f}")