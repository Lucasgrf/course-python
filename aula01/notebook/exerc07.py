# Solicite ao usuário que insira sua data de nascimento e calcule sua idade.

import datetime

dataNascimento = input("Insira sua data de nascimento (dd/mm/aaaa): ")
dataNascimento = datetime.datetime.strptime(dataNascimento, "%d/%m/%Y") 
dataAtual = datetime.datetime.now()
idade = dataAtual.year - dataNascimento.year
if (dataAtual.month < dataNascimento.month):
    idade -= 1
print(f"Você tem {idade} anos.")
