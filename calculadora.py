
#def soma(num1, num2):
#    return(num1+num2)

#def sub(num1, num2):
#    return(num1-num2)

#def mult(num1,num2):
#    return(num1*num2)

#def div(num1,num2):
#    if num2 !=0:
#        return num1/num2
#    return 'Não existe divisão por 0'

def sair(*args):
    exit()
  
opcoes = {'1':lambda x,y: x+y,
          '2':lambda x,y: x-y,
          '3':lambda x,y: x*y,
          '4':lambda x,y: x/y,
          '5':lambda x,y: exit()
          }


def inicio():
    while True:
        n1 = float(input('Digite o n1: '))
        n2 = float(input('Digite o n2: '))

        print(f'Digite a opção desejada: \n1 - Soma\n' \
                f'2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - sair')

        opt = input('Escolha: ')

        if opt in opcoes.keys():
            print(opcoes[opt](n1,n2))
        else:
            print('Opção invalida')




if __name__=='__main__':
    inicio()