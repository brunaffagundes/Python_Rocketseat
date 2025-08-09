# pip install.requests==2.31.0

print("\nImportação e uso de um módulo de terceiros")
import requests
url = "https://www.exemple.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")