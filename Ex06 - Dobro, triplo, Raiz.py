import math
num = int(input('Digite um numero:'))
dobro = num*2
triplo = num*3
raiz = num ** (1/2)
print('O dobro de {} é {}.\n O triplo é {}.\n A raiz é {}.'.format(num,dobro,triplo,math.ceil(raiz)))