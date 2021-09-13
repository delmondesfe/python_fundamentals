def soma(x,y):
    return x+y

def divisao(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'Não existe divisão por zero'