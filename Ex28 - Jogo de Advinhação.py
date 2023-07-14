from time import sleep
import random

num1 = int(input('Digite o numero que você acha que estou pensando de 1 a 5:'))
for c in range(1,3):
    print('Pensando...')
    sleep(1.2)
num2 = random.randint(1,5)

if num1 == num2:
    print('Parabens eu estava pensando justamente no numero {}'.format(num1))
elif num1 >= num2:
    print('Não... Eu estava pensando no numero {}'. format(num2))
elif num1 <= num2:
    print('Não... Eu estava pensando no numero {}'. format(num2))

