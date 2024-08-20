# Crie um programa que solicite ao usuário o valor total 
# de sua compra. Aplique um desconto de 10% no total da compra. Imprima o valor após o desconto.
valorTotal = float(input("Insira o valor total da compra: "))
desconto = valorTotal * 0.10
valorComDesconto = valorTotal - desconto
print(f"O valor total da compra é R$ {valorTotal:.2f}. Após o desconto de 10%, o valor é R$ {valorComDesconto:.2f}.")