# @classmethod - usado principalmente para criar instâncias a partir de configurações globais
# @staticmethod

class MinhaClasse:
    valor = 10 # atributo da classe 
    
    def __init__(self, nome) -> None:
        self.nome = nome # atributo da instância

    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"

    @classmethod
    def metodo_classe(cls):
        return f"Método da classe chamado para valor = {cls.valor}"

    @staticmethod # não recebe argumentos, logo não tem acesso aos atributos da instância e nem da classe, mas executa uma ação especifíca
    def metodo_estatico():
        return "Método estático chamado"

obj = MinhaClasse(nome="classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

# Exemplo 01

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(2022))

configuracao1 = "Toyota, Corolla,2022"
carro1 =  Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo:{carro1.modelo}\nAno: {carro1.ano}")


# Exemplo 02 - @staticmethod

class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b

print(Matematica.somar(a=10, b=15))
