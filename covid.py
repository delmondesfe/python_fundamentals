with open('Dados-covid-19-estado.csv') as arquivo:
    dados = arquivo.readlines()


filtro = '01/jul'

for registro in dados:
    if filtro in registro.split(';')[0]:
        print('data: ',registro.split(';')[0])
        print('Total de casos:',registro.split(';')[1])
        print('casos por dia: ',registro.split(';')[2])
        print('Obitos por dia: ',registro.split(';')[3])
