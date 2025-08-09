# Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito. O resultado da aplicação deve ser apresentado no terminal.

### Regras da aplicação
"""
- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
    - Nome
    - Telefone
    - Email
    - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato
"""
def adicionar_contato(contatos, nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    print(f"Contato '{nome}' adicionado com sucesso!")


def ver_contatos(contatos):
    print("\nLista de contatos:")
    if not contatos:
        print("Nenhum contato cadastrado.")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else " "
        print(f"{indice}. [{status}] {contato['nome']} - {contato['telefone']} - {contato['email']}")


def editar_contato(contatos, indice, novo_nome, novo_tel, novo_email):
    indice_ajustado = int(indice) - 1
    if 0 <= indice_ajustado < len(contatos):
        contatos[indice_ajustado]["nome"] = novo_nome
        contatos[indice_ajustado]["telefone"] = novo_tel
        contatos[indice_ajustado]["email"] = novo_email
        print(f"Contato {indice} atualizado com sucesso!")
    else:
        print("Índice de contato inválido.")


def alternar_favorito(contatos, indice):
    indice_ajustado = int(indice) - 1
    if 0 <= indice_ajustado < len(contatos):
        contatos[indice_ajustado]["favorito"] = not contatos[indice_ajustado]["favorito"]
        status = "favorito" if contatos[indice_ajustado]["favorito"] else "não favorito"
        print(f"Contato {indice} agora é {status}.")
    else:
        print("Índice de contato inválido.")


def ver_favoritos(contatos):
    print("\nContatos favoritos:")
    favoritos = [c for c in contatos if c["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito.")
    for indice, contato in enumerate(favoritos, start=1):
        print(f"{indice}. ★ {contato['nome']} - {contato['telefone']} - {contato['email']}")


def deletar_contato(contatos, indice):
    indice_ajustado = int(indice) - 1
    if 0 <= indice_ajustado < len(contatos):
        removido = contatos.pop(indice_ajustado)
        print(f"Contato '{removido['nome']}' deletado com sucesso!")
    else:
        print("Índice de contato inválido.")


# Programa principal
contatos = []

while True:
    print("\nAgenda de Contatos")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar favorito")
    print("5. Ver favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        adicionar_contato(contatos, nome, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice = input("Digite o número do contato a editar: ")
        novo_nome = input("Novo nome: ")
        novo_tel = input("Novo telefone: ")
        novo_email = input("Novo e-mail: ")
        editar_contato(contatos, indice, novo_nome, novo_tel, novo_email)

    elif escolha == "4":
        ver_contatos(contatos)
        indice = input("Digite o número do contato para alterar favorito: ")
        alternar_favorito(contatos, indice)

    elif escolha == "5":
        ver_favoritos(contatos)

    elif escolha == "6":
        ver_contatos(contatos)
        indice = input("Digite o número do contato para deletar: ")
        deletar_contato(contatos, indice)

    elif escolha == "7":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
