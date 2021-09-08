#carregando o arquivo
from typing import Container


arquivo = open('arquivo.txt', 'r')


#acessando o arquivo
#conteudo = arquivo.read()

#quebrando por linhas
conteudo = arquivo.readlines()


#sempre fechar a conexão
arquivo.close()

print(conteudo)