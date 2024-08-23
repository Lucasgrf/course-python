#Crie um programa que classifique uma pessoa em uma das seguintes categorias com base na idade:

#Criança (0-12 anos)
#Adolescente (13 a 17 anos)
#Adulto (18-64 anos)
#Idosos (65 anos ou mais)

age = int(input("Digite a idade: "))

if(age < 0):
    print("Idade inválida")
elif age < 12:
    print("Criança")
elif age < 18:
    print("Adolescente")
elif age < 65:
    print("Adulto")
else:
    print("Idoso")