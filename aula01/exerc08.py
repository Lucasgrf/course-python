# Solicite ao usuário que insira seu nome e sobrenome. Em seguida, 
# gere um e-mail concatenando a inicial do nome com o sobrenome seguido de “@gmail.com”. O e-mail deve estar todo em letras minúsculas.

nome = input("Insira seu nome: ")
sobrenome = input("Insira seu sobrenome: ")
email = f"{nome[0].lower()}{sobrenome.lower()}@gmail.com"
print(email)