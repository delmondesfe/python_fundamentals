arquivo = open('arquivo.txt','w')

conteudo = arquivo.readlines()

arquivo.close()

conteudo.append('nova linha')

arquivo = open('arquivo.txt','w')

arquivo.writelines(conteudo)

arquivo.close()


