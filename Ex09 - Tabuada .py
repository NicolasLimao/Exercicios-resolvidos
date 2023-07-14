from time import sleep
num = int(input('Digite um numero para ver a tabuada:'))
for c in range (1,11):
    print('{} x {} = {}'.format(num, c, num*c))
    sleep(1)
