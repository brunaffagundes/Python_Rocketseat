# É uma coleção não ordenada de pares chave-valor

# Criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
print("Meu dicionário:", pessoa)

# Acessando valor por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = "35"
print("Idade atualizada:", pessoa["idade"])

# Removendo um par de chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), values(), items()
chaves = pessoa.keys()
chaves = list(pessoa.keys())
print("Chaves:", chaves)
print("Primeira chave:", chaves[0])

# Métodos values
valores = pessoa.values()
valores = list(pessoa.values())
print("Valores:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Métodos items
itens = pessoa.items()
itens = list(pessoa.items())
print("Pares chave-valor do dicionário", itens)
print("Primeiro par chave-valor:", itens[0][1])
print("Primeiro par chave-valor:", "%s = %s" % (itens[0][0], itens[0][1]))