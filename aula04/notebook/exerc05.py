# Existe uma classe chamada ReprodutorMusica que gerencia a reprodução de músicas, a criação de listas de reprodução e a 
# geração de recomendações. Refatore a classe para respeitar o princípio da responsabilidade única.
        
class Musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
    
    def __str__(self):
        return f'{self.titulo} por {self.artista}'

class Reprodutor:
    def __init__(self):
        self.musica_atual = None
    
    def reproduzir(self, musica):
        self.musica_atual = musica
        print(f'Reproduzindo: {musica}')
        
class ListaReproducao:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []
    
    def adicionar_musica(self, musica):
        self.musicas.append(musica)
    
    def listar_musicas(self):
        for musica in self.musicas:
            print(musica)

class Recomendador:
    def gerar_recomendacoes(self, preferencias):
        # Não entendi muito bem o que fazer aqui
        print('Gerando recomendações...')


musica1 = Musica('Imagine', 'John Lennon')
musica2 = Musica('Bohemian Rhapsody', 'Queen')

reprodutor = Reprodutor()
lista_reproducao = ListaReproducao('Favoritas')
# recomendador = Recomendador()

lista_reproducao.adicionar_musica(musica1)
lista_reproducao.adicionar_musica(musica2)

print('Lista de Reprodução:')
lista_reproducao.listar_musicas()

reprodutor.reproduzir(musica1)

# recomendador.gerar_recomendacoes(preferencias=None)
