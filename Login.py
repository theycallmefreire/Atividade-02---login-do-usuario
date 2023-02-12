class User:
    def __init__(self, nome, email, senha):
        self.name = nome
        self.email= email
        self.senha = senha
    def autorizacao(self):
        return f'Muito bem {self.name} seu cadastro esta completo!'
