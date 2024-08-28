# Existe uma classe chamada EstoqueHardware que trata do gerenciamento de produtos, pedidos e geração de relatórios de vendas. 
# Refatore a classe para respeitar o princípio da responsabilidade única.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def __str__(self):
        return f'{self.nome} - Preço: {self.preco}, Quantidade: {self.quantidade}'
    
class GerenciadorEstoque:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f'Produto {produto.nome} adicionado ao estoque.')
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)

class Pedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
    
    def __str__(self):
        return f'Pedido - Produto: {self.produto.nome}, Quantidade: {self.quantidade}'

class GerenciadorPedidos:
    def __init__(self):
        self.pedidos = []
    
    def realizar_pedido(self, produto, quantidade):
        if produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            pedido = Pedido(produto, quantidade)
            self.pedidos.append(pedido)
            print(f'Pedido realizado: {pedido}')
        else:
            print('Quantidade insuficiente no estoque.')
    
    def listar_pedidos(self):
        for pedido in self.pedidos:
            print(pedido)

class GeradorRelatorios:
    def gerar_relatorio_vendas(self, pedidos):
        print('Relatório de Vendas:')
        for pedido in pedidos:
            print(f'Produto: {pedido.produto.nome}, Quantidade: {pedido.quantidade}, Total: {pedido.produto.preco * pedido.quantidade}')


produto1 = Produto('Mouse', 50.0, 100)
produto2 = Produto('Teclado', 150.0, 50)

gerenciador_estoque = GerenciadorEstoque()
gerenciador_pedidos = GerenciadorPedidos()
gerador_relatorios = GeradorRelatorios()

gerenciador_estoque.adicionar_produto(produto1)
gerenciador_estoque.adicionar_produto(produto2)

print('Estoque:')
gerenciador_estoque.listar_produtos()

gerenciador_pedidos.realizar_pedido(produto1, 10)
gerenciador_pedidos.realizar_pedido(produto2, 5)

print('Pedidos:')
gerenciador_pedidos.listar_pedidos()

gerador_relatorios.gerar_relatorio_vendas(gerenciador_pedidos.pedidos)

