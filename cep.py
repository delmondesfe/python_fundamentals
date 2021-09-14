import requests


while True:
    try:

        url = 'https://viacep.com.br/ws/{cep}/json/'
        numero = input('Digite o CEP: ')
        resposta = requests.get(url.format(cep = numero))

        resposta_format = resposta.json()
        

        print('status: ', resposta.status_code)
        print('Logradouro: ',resposta_format['logradouro'])
        print('Bairro: ',resposta_format['bairro'])
        print('UF: ',resposta_format['uf'])
        print('DDD: ',resposta_format['ddd'])

    except KeyError:
        print('CEP INVALIDO')
    except Exception as err:
        print('Digite outro valor')