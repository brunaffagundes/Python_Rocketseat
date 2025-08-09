print("Exemplo de captura de exceções")
try:
  numero = int(input("Digite um número inteiro: "))
  resultado = 10 / numero
except ValueError as e:
   print(f"Erro de Value error: {e}")
   raise ValueError("Tipos de varoáveis incompativeis")
except Exception as e:
   print(f"Erro: {e}")
else:
   print(f"Resultado: {resultado}")
finally:
   print("Operação finalizada")