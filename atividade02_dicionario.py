# Autor : Jhonatan
# Projeto : Uso de API (conceito de dicionario)

# requisições http - get
import requests

#uso da APAI do ViaCEP
cep = input("Digite seu CEP (somente números): ").strip().replace("-", "")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

print(f"Longradouro: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Cidade: {dados['localidade']}")