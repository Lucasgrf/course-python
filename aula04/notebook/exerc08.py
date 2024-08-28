class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
    
    def __str__(self):
        return self.descricao

class ListaTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, descricao):
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)
        print(f'Tarefa "{descricao}" adicionada com sucesso.')
    
    def listar_tarefas(self):
        if not self.tarefas:
            print('Nenhuma tarefa pendente.')
        else:
            print('Tarefas Pendentes:')
            for i, tarefa in enumerate(self.tarefas, start=1):
                print(f'{i}. {tarefa}')
    
    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa_removida = self.tarefas.pop(indice)
            print(f'Tarefa "{tarefa_removida}" removida com sucesso.')
        else:
            print('Índice inválido.')

def main():
    lista_tarefas = ListaTarefas()
    
    while True:
        print('\n1 - Adicionar tarefa')
        print('2 - Listar tarefas')
        print('3 - Remover tarefa')
        print('4 - Sair')
        opcao = input('Digite a opção desejada: ')
        
        if opcao == '1':
            descricao = input('Digite a descrição da tarefa: ')
            lista_tarefas.adicionar_tarefa(descricao)
        
        elif opcao == '2':
            lista_tarefas.listar_tarefas()
        
        elif opcao == '3':
            indice = int(input('Digite o índice da tarefa a ser removida: ')) - 1
            lista_tarefas.remover_tarefa(indice)
        
        elif opcao == '4':
            break
        
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()