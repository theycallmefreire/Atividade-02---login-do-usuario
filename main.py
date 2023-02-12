#Atividade 02 - identifique dentro do projeto de vocês um objeto, tenta entender como o objeto funcionará dentro do sistema e crie uma classe para ele, para criação da classe pode utilizar qualquer plataforma que acharem mais conveniente
from Login import User

print("----Bem Vindo!----\nNovo por aqui? Crie já sua conta!")

nome = input("Digite seu nome:")
email = input('Digite seu email:')
senha = input("Digite a sua senha:")

usuario = User(nome, email, senha)
print(usuario.autorizacao())
