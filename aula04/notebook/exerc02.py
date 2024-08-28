# Escreva um programa muito básico semelhante a Netflix que permite adicionar filmes ou séries a uma lista de favoritos. 
# Também inclua um método que permita ver quais filmes ou séries estão na lista de favoritos. Não se esqueça de usar classes.

class Item:
    def __init__(self, titulo, tipo):
        self.titulo = titulo
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.tipo}: {self.titulo}'

class Favoritos:
    def __init__(self):
        self.itens = []
    
    def adicionar(self, item):
        self.itens.append(item)
        print(f'{item.tipo} "{item.titulo}" adicionado aos favoritos.')
    
    def listar_favoritos(self):
        if not self.itens:
            print('Nenhum item na lista de favoritos.')
        else:
            print('Favoritos:')
            for item in self.itens:
                print(item)

favoritos = Favoritos()

while True:
    print('\n1 - Adicionar filme ou série aos favoritos')
    print('2 - Listar favoritos')
    print('3 - Sair')
    opcao = input('Digite a opção desejada: ')
    
    if opcao == '1':
        titulo = input('Digite o título do filme ou série: ')
        tipo = input('Digite o tipo (Filme/Série): ')
        item = Item(titulo, tipo)
        favoritos.adicionar(item)
        
    elif opcao == '2':
        favoritos.listar_favoritos()
    
    elif opcao == '3':
        break
    
    else:
        print('Opção inválida')
