# Bloco de código reutilizável

def saudacao(nome):
  print(f"Olá, {nome}!")

print("\n Chamando a função saudacao:")
saudacao("Bob")
saudacao("João")

# Função com retorno
def quadrado(numero):
        resultado = numero ** 2
        return resultado
        
print("\nChamando a função quadrado")
resultado_quadrado = quadrado(5)
print("Resultado da função quadrado:", resultado_quadrado)

# Função com múltplos parametros
def soma(numero1, numero2):
        resultado = numero1 + numero2
        return resultado

print("\nChamando a função soma")
resultado_soma = soma(10, 20)
print("Resultado da função soma:", resultado_soma)