from time import sleep

print ('-=°'*5, 'Tabuada v2.0','°=-'*5)

num = int(input('Digite um numero para ver a tabuada:'))
for a in range (1,3):
    print('Carregando...')
    sleep(1)

for c in range (1,11):
    print('{} x {} = {}'.format(num, c, num*c))
    sleep(1)
