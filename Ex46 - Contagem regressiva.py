""" Contagem regressiva """

import time
a = str(input('Digite sim ou não para começar a contagem regressiva:'))
if a == ('sim'):
    for c in range(10,1,-1):
        print(c)
        time.sleep(1)
    print('1')
    time.sleep(1)
    print('\33[31m Feliz Ano Novo !!')
elif a == ('nao'):
    print('Tudo bem.')