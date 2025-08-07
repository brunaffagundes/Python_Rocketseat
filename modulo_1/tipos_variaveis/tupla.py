# Coleção ordenada e imutável de elementos (depois de declarar, não dá par alterar)

# Criando uma tupla de exemplo
minha_tupla = (1, 2, 3, 4)
print("Minha tupla:", minha_tupla)

print("Minha tupla[0]:", minha_tupla[0])
print("Minha tupla[-1]:", minha_tupla[-1])

# Método Count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

# Método Index
indice = minha_tupla.index(3)
print("Índice do elemento 3:", indice)