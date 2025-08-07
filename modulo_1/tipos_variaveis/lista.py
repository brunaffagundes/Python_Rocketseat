# Lista é uma coleção de elementos ordenáveis e mutáveis

# Declaração
"""minha_lista = [1, 2, 3, 4, 5, "rockeseat", True, False]"""
minha_lista = [1, 2, 3, 4, 5, 6, 9, 112]

# Exibibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibibindo a lista
minha_lista[0] = "python"
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[4]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])

# Métodos de Lista

# Método append(): Adiciona um novo elemento ao final da lista
minha_lista.append(6)
print("minha_lista.append(6):", minha_lista)

# Método index
indice = minha_lista.index(5)
print("minha_lista.index(5):", indice)

# Método insert: Insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("minha_lista.insert(2, 10):", minha_lista)

# Método pop
elemento_removido = minha_lista.pop(2)
print("minha_lista.pop(2):", minha_lista)

#Método remove
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# Método sort
minha_lista.sort()
print("Após sort():", minha_lista)