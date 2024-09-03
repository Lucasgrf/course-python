class Leitor:
    def __init__(self, nome: str):
        self.nome = nome
        self.livros_lidos = 0
        self.historico_livros = []

    def __str__(self):
        return f"Leitor: {self.nome} - Livros lidos: {self.livros_lidos} - Histórico: {[livro.titulo for livro in self.historico_livros]}"

    def ler_livro(self, livro):
        self.livros_lidos += 1
        self.historico_livros.append(livro)


class Categoria:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome


class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, categoria: Categoria):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.disponivel = True

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Ano: {self.ano} - Categoria: {self.categoria}"


class Catalogo:
    def __init__(self, nome: str):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def buscar_livro(self, termo: str):
        resultados = [livro for livro in self.livros if termo.lower() in livro.titulo.lower() or
                      termo.lower() in livro.autor.lower() or termo.lower() in livro.categoria.nome.lower()]
        return resultados


class MagicBooks:
    def __init__(self):
        self.catalogos = []
        self.leitores = []

    def criar_catalogo(self, nome: str):
        catalogo = Catalogo(nome)
        self.catalogos.append(catalogo)
        return catalogo

    def adicionar_leitor(self, nome: str):
        leitor = Leitor(nome)
        self.leitores.append(leitor)
        return leitor

    def buscar_livro(self, termo: str):
        for catalogo in self.catalogos:
            resultados = catalogo.buscar_livro(termo)
            if resultados:
                return catalogo, resultados
        return None, []

    def adicionar_livro(self, catalogo: Catalogo, livro: Livro):
        catalogo.adicionar_livro(livro)

    def pedir_livro(self, leitor: Leitor, termo: str):
        catalogo, resultados = self.buscar_livro(termo)
        if resultados:
            livro = resultados[0] # Pega o primeiro resultado da lista
            if livro.disponivel:
                livro.disponivel = False
                leitor.ler_livro(livro)
                print(f"\nO leitor {leitor.nome} pegou o livro '{livro.titulo}' com sucesso!\n")
            else:
                print(f"\nO livro '{livro.titulo}' não está disponível no momento.\n")
        else:
            print(f"\nLivro '{termo}' não encontrado. Criando novo catálogo e adicionando.\n")
            novo_catalogo = self.criar_catalogo("Novo Catalogo")
            novo_livro = Livro(termo, "Autor Desconhecido", 2024, Categoria("Desconhecido"))
            self.adicionar_livro(novo_catalogo, novo_livro)
            self.pedir_livro(leitor, termo)  # Repetir o processo com o novo catálogo

    def listar_livros(self):
        print("\n=== Listagem de Livros ===")
        for catalogo in self.catalogos:
            print(f"\nCatálogo: {catalogo.nome}\n")
            for livro in catalogo.livros:
                print(livro)
        print("\n=== Fim da Listagem ===\n")

    def menu(self):
        while True:
            print("\n=== Menu da Biblioteca ===")
            print("1. Listar livros")
            print("2. Buscar livro")
            print("3. Adicionar livro ao catálogo")
            print("4. Criar novo catálogo")
            print("5. Criar novo leitor")
            print("6. Pedir livro")
            print("7. Sair")
            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.listar_livros()
            elif opcao == "2":
                termo = input("\nDigite o termo de busca (título, autor ou categoria): ")
                catalogo, resultados = self.buscar_livro(termo)
                if resultados:
                    print(f"\nLivros encontrados no catálogo '{catalogo.nome}':")
                    for livro in resultados:
                        print(livro)
                    print()
                else:
                    print("\nNenhum livro encontrado.\n")
            elif opcao == "3":
                titulo = input("\nDigite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                ano = int(input("Digite o ano do livro: "))
                categoria_nome = input("Digite o nome da categoria: ")
                categoria = Categoria(categoria_nome)
                livro = Livro(titulo, autor, ano, categoria)
                catalogo_nome = input("Digite o nome do catálogo para adicionar o livro: ")
                catalogo = next((cat for cat in self.catalogos if cat.nome == catalogo_nome), None)
                if catalogo:
                    self.adicionar_livro(catalogo, livro)
                    print("\nLivro adicionado com sucesso!\n")
                else:
                    print("\nCatálogo não encontrado.\n")
            elif opcao == "4":
                nome = input("\nDigite o nome do novo catálogo: ")
                self.criar_catalogo(nome)
                print("\nNovo catálogo criado com sucesso!\n")
            elif opcao == "5":
                nome = input("\nDigite o nome do novo leitor: ")
                self.adicionar_leitor(nome)
                print("\nNovo leitor criado com sucesso!\n")
            elif opcao == "6":
                leitor_nome = input("\nDigite o nome do leitor: ")
                leitor = next((leitor for leitor in self.leitores if leitor.nome == leitor_nome), None)
                if leitor:
                    termo = input("Digite o título do livro que deseja pedir: ")
                    self.pedir_livro(leitor, termo)
                else:
                    print("\nLeitor não encontrado.\n")
            elif opcao == "7":
                print("\nSaindo do sistema...\n")
                break
            else:
                print("\nOpção inválida. Tente novamente.\n")

biblioteca = MagicBooks()
catalogo_principal = biblioteca.criar_catalogo("Biblioteca Principal")

livros = [
    Livro("Harry Potter", "J.K. Rowling", 1997, Categoria("Fantasia")),
    Livro("Senhor dos Anéis", "J.R.R. Tolkien", 1954, Categoria("Fantasia")),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, Categoria("Infantil")),
    Livro("Dom Casmurro", "Machado de Assis", 1899, Categoria("Romance")),
    Livro("O Hobbit", "J.R.R. Tolkien", 1937, Categoria("Fantasia")),
    Livro("O Código da Vinci", "Dan Brown", 2003, Categoria("Suspense")),
    Livro("O Alquimista", "Paulo Coelho", 1988, Categoria("Autoajuda")),
    Livro("O Diário de Anne Frank", "Anne Frank", 1947, Categoria("Biografia")),
    Livro("A Menina que Roubava Livros", "Markus Zusak", 2005, Categoria("Drama")),
    Livro("O Nome do Vento", "Patrick Rothfuss", 2007, Categoria("Fantasia")),
    Livro("A Culpa é das Estrelas", "John Green", 2012, Categoria("Romance")),
    Livro("O Iluminado", "Stephen King", 1977, Categoria("Terror")),
    Livro("A Revolução dos Bichos", "George Orwell", 1945, Categoria("Política")),
    Livro("1984", "George Orwell", 1949, Categoria("Política")),
    Livro("A Metamorfose", "Franz Kafka", 1915, Categoria("Drama")),
    Livro("O Senhor das Moscas", "William Golding", 1954, Categoria("Drama")),
    Livro("O Médico", "Noah Gordon", 1986, Categoria("Histórico")),
    Livro("O Poder do Hábito", "Charles Duhigg", 2012, Categoria("Autoajuda")),
    Livro("O Ladrão de Raios", "Rick Riordan", 2005, Categoria("Fantasia"))
]

for livro in livros:
    biblioteca.adicionar_livro(catalogo_principal, livro)

biblioteca.menu()
