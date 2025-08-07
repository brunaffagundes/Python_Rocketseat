# Loop é uma condição que permite repetir um bloco de código enquanto uma condição for verdadeira

# for é utilizado para iterar sobre uma sequência de elementos ( vai repetir a mesma ação para cada elemento de uma sequência)
print ( "for utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
        print(elemento)

print ( "for utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
        print(elemento)
        
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
        print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
        print(valor)

for chave, valor in pessoa.items():
        print(chave, valor)
        
# range (): intervalo numérico
# [0,1,2,3,4]
print("\n Utilizando range()")
print(list(range(0,10)))
for numero in range(5):
        print(numero)
        
print("\n Utilizando range() com len()")
lista = [1,2,3,4,5]
for indice in range(0, len(lista)):
        print("Índice:", indice)
        print("elemento: ", lista[indice])
        if indice == 3:
                lista[indice] = 5
        print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
        print(indice, valor)
        if indice == 1:
                print("ÍNDICE 1")