import random
from time import sleep


lista = [('45401384807','Felipe'),
         ('45401324907','Carlos'),
         ('45121112021','Alberto'),
         ('44412125212','Leonardo'),
         ('77474511052','Bruno'),
         ('11120203225','Davi')]


num_cadeiras = len(lista)-1

while num_cadeiras != 0:
    print('Musica tocando...')
    sleep(1)
    print('Musica parou')
    sleep(1)
    print('Jogadores se movimentam')
    sleep(3)
    random.shuffle(lista)
    print(f'O jogador {lista.pop()} saiu do jogo')

    num_cadeiras -= 1


        