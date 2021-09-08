with open('arquivo.txt') as arquivo:
    conteudo = arquivo.read()

conteudo += 'qualquer coisa \n'

with open('arquivo.txt','a') as arquivo:
    arquivo.write(conteudo)
    

print(conteudo)