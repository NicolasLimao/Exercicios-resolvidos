#sortear um exercicio de 01 a 50

import random
from time import sleep

nome = str(input('qual o seu nome ? ')).strip ()
for a in range (0,2):
    print('procurando no banco de dados...')
    sleep (1)
print ('Tudo bem {} vou escolher um exercicio para voce revisar'.format (nome))
exercicio= random.randint(1,51)
for c in range (0,3):
    print('Escolhendo...')
    sleep (2)
print ('achei... Você deve revisar o exercicio {} '.format (exercicio))

