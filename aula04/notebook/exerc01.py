#  Escreva um programa que permita que vários alunos se matriculem em uma disciplina. 
# Também inclua um método que permita ver quais alunos estavam matriculados na referida disciplina. Não se esqueça de usar classes.

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'
    
class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        
    def __str__(self):
        return f'Disciplina: {self.nome}'
    
    def matricular(self, aluno):
        self.alunos.append(aluno)
    
    def listar_alunos(self):
        print('\n', self)
        if not self.alunos:
            print('Nenhum aluno matriculado.')
        else:
            for aluno in self.alunos:
                print(aluno)

disciplina = Disciplina('POO com Python')

while True:
    print('\n1 - Matricular aluno')
    print('2 - Listar alunos matriculados')
    print('3 - Sair')
    opcao = input('Digite a opção desejada: ')
    
    if opcao == '1':
        nome = input('Digite o nome do aluno: ')
        idade = int(input('Digite a idade do aluno: '))
        aluno = Aluno(nome, idade)
        disciplina.matricular(aluno)
        print('\nAluno matriculado com sucesso!')
        
    elif opcao == '2':
        disciplina.listar_alunos()
    
    elif opcao == '3':
        break
    
    else:
        print('Opção inválida')

