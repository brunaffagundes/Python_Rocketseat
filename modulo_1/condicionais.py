# if (se), elif (outra condição), else(se não)

# Exemplo de "if"
idade = int(input("Digite sua idade: "))
idade = int(idade)
if idade >= 18:
        print("Você é maior de idade.")   
elif idade >= 12:
        print("Você é adolescente")
else:
        print("Você é menor de idade")
        
mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)