def soma(a,b):

    try:
        return a + b
    except TypeError:
        print('a e b devem ser do tipo int ou float')

def subtracao(a,b):

    try:
        return a - b
    except TypeError:
        print('a e b devem ser do tipo int ou float')

def multiplicacao(a,b):

    try:
        return a * b
    except TypeError:
        print('a e b devem ser do tipo int ou float')

def divisao(a,b):
    try:
        return a/b
    except TypeError:
        print('a e b devem ser do tipo int ou float')
    except ZeroDivisionError:
        print('b deve ser diferente de zero')