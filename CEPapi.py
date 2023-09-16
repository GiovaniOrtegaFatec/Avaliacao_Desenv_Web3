import requests

print('Consulta de CEP')
print()

cep_consulta = input('Digite o CEP: ')  # pede para digitar o CEP desejado

if len(cep_consulta) != 8:  # se a quantidade de dígitos do CEP for diferente de 8 então...
    print('O CEP deve conter 8 dígitos!')
    exit()
    
url = f'https://viacep.com.br/ws/{cep_consulta}/json/' 
response = requests.get(url) #a resposta fica armazenada na variável

#https://www.gov.br/conecta/catalogo/apis/cep-codigo-de-enderecamento-postal/swagger-json/swagger_view

if response.status_code == 200: #verifica se a requisição deu certo
    data = response.json() #converteu os dados para biblioteca json
    if 'erro' not in data:
        print('CEP encontrado:')
        print(f'CEP: {data["cep"]}') #exibe o CEP
        print(f'Logradouro: {data["logradouro"]}') #exibe o logradouro (rua)
        print(f'Complemento: {data["complemento"]}') #exibe se há complemento
        print(f'Bairro: {data["bairro"]}') #exibe o bairro 
        print(f'Cidade: {data["localidade"]}') #exibe o município
        print(f'Estado: {data["uf"]}') #exibe
    elif 'erro' in data:
        print('CEP inválido')
elif response.status_code == 404:
    error_data = response.json()
    print(f'Erro 404: {error_data["message"]}')
elif response.status_code == 400:
    error_data = response.json()
    print(f'Erro 400: {error_data["message"]}')
else:
    print('Erro ao consultar o CEP. Verifique sua conexão com a internet ou tente novamente mais tarde.')
