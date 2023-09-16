import requests

print('Consulta municípios da Unidade Federativa')

siglaUF = input('Digite a sigla da Unidade Federativa: ')

if len(siglaUF) != 2:
    print('A sigla deve conter apenas 2 dígitos')
    exit()

url = f'https://brasilapi.com.br/api/ibge/municipios/v1/{siglaUF}?providers=dados-abertos-br,gov,wikipedia'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if 'erro' not in data:
        print('Municípios da Unidade Federativa:', siglaUF)
        for municipio in data:
            print('Município: ', municipio['nome'])
            print('Código IBGE: ', municipio['codigo_ibge'])
            print()
    else:
        error_data = data['erro']
        print(f'Erro: {error_data["message"]}')
elif response.status_code == 404:
    error_data = response.json()
    print(f'Erro 404: {error_data["message"]}')
else:
    print(f'Erro ao consultar a Unidade Federativa! Código de resposta: {response.status_code}')



