# Declaração
nome_completo = "Bruna Fagundes"

nome_completo_aspas = """bruna
fagundes""" #permite pular linhas

nome_completo_quebra = "Bruna \
Fagundes"

nome = "bruna"
sobrenome = "fagundes"

# Formatação de string"
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Bruna" + " " + "Fagundes")
print("Nome completo (4a forma):" + "Bruna", "Fagundes")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print("Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))