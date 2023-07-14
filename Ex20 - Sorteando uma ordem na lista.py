import random
from time import sleep

nomes = []

for i in range(1,5):
    nome = input('Digite o {}° nome:'.format(i))
    nomes.append(nome)
random.shuffle(nomes)
print('Muito bem, sendo assim... A ordem de apresentação dos trabalhos será está...')
for c in range(1,3):
    print('Embaralhando..')
    sleep(1.2)
print(nomes)