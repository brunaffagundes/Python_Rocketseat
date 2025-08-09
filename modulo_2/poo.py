# Programação Orientada à objetos é um paradigma de programação que se baseia na organização dos problemas em torno de objetos

# Objetos são instâncias de classes

# Uma classe é um modelo, um plano que define a estrutura desses objetos (atributos e métodos)

# Classes Exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    def saudacao(self):
        return("Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
        
# Objetos - representar coisas do mundo real
pessoa1 = Pessoa("João", 25)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Maria", idade=32)
mensagem = pessoa2.saudacao()
print(mensagem)