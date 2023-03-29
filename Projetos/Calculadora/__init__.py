from funcoes import soma, subtracao, multiplicacao, divisao

def calcule(operador):
    try:
        a = float(input('Entre com o valor de a: '))
        b = float(input('Entre com o valor de b: '))

    except TypeError:
        print('a e b devem conter valores numéricos!')

    if operador == '+' or 'soma':
        return soma(a,b)
    elif operador == '-' or 'subtracao':
        return subtracao(a,b)
    elif operador == '*' or 'multiplicacao':
        return multiplicacao(a,b)
    elif operador =='/' or 'divisao':
        return divisao(a,b)
    else:
        print('insira um operador válido')