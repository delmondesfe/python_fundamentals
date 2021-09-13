opcoes = {'1':lambda x,y: x+y,
          '2':lambda x,y: x-y,
          '3':lambda x,y: x*y,
          '4':lambda x,y: x/y,
          '5':lambda x,y: exit()
          }



while True:
        
        try:
            n1 = float(input('Digite o n1: '))
            n2 = float(input('Digite o n2: '))

            op = input(f'Digite a opção desejada: \n' \
                   f'1 - Soma\n' \
                   f'2 - Subtração\n' \
                   f'3 - Multiplicação\n' \
                   f'4 - Divisão\n' \
                   f'5 - sair \n' \
                   f'Escolha: ')

            res = opcoes[op](n1,n2)
        except ZeroDivisionError:
            print('Não é possível dividir um número por zero')

        except KeyError:
            print('Valor opção invalida')
        
        except ValueError:
            print('Digite apenas numeros')

        except Exception as err:
            print('Erro desconhecido', err)

        else:
            print(res)

        finally:
            print('Passei por aqui')