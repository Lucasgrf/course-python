#Crie um programa que classifique as notas de um aluno em duas disciplinas e imprima se o aluno for aprovado em ambas as disciplinas.

#O aluno é aprovado se obtiver nota igual ou superior a 60 em cada disciplina.
#Caso o aluno falte em alguma delas, poderá realizar exame de nivelamento. Se for o caso, imprima que deve fazer a prova da disciplina específica.
#Se perder ambas, deverá imprimir reprovado.
#A faixa de pontuação é de 0 a 100.

faltas1 = bool(int(input("Digite 1 se faltou na primeira disciplina ou 0 se não faltou: ")))
faltas2 = bool(int(input("Digite 2 se faltou na segunda disciplina ou 0 se não faltou: ")))

nota1 = 0
nota2 = 0
reposicao = 0

while nota1 ==0:
    if(faltas1 and faltas2):
        print("Reprovado")
        break

    if(faltas1):
        print("Deve fazer a prova da primeira disciplina")
        nota2 = int(input("Digite a nota da segunda disciplina: "))
        reposicao = int(input("Digite a nota da reposição da primeira prova: "))
    if(faltas2):
        print("Deve fazer a prova da segunda disciplina")
        nota1 = int(input("Digite a nota da primeira disciplina: "))
        reposicao = int(input("Digite a nota da reposição da segunda prova: "))

    if(reposicao == 0):
        nota1 = int(input("Digite a nota da primeira disciplina: "))
        nota2 = int(input("Digite a nota da segunda disciplina: "))
    elif(nota1 == 0 and faltas1 > 0):
        nota1 = reposicao
    elif(nota2 == 0 and faltas2 > 0):
        nota2 = reposicao

    if(nota1 >= 60 and nota2 >= 60):
        print("Aprovado em ambas disciplinas.")
    elif(nota1 >= 60 and nota2 < 60):
        print("Aprovado apenas primeira disciplina.")
    elif(nota1 < 60 and nota2 >= 60):
        print("Aprovado apenas segunda disciplina.")
    else:
        print("Reprovado em ambas disciplinas.")