from time import sleep
num = int(input('Descubra o fatorial de um número: '))
for c in range(1,4):
    print('Carregando...')
    sleep(1.2)
counter = num
fat = 1

print('Calculando o numero {}'.format(num))
for a in range(1,3):
    print('Calculando...')
    sleep(1.2)
while counter > 0:
    print("{}".format(counter), end="")
    fat *= counter
    counter -= 1
    print(" x " if counter > 0 else " = ", end="")
print("{}".format(fat))