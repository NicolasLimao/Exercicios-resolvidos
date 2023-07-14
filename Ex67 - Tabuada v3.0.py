from time import sleep

while True:
    num = int(input('Digite um numero para ver a tabuada:'))
    for c in range (1,11):
        print(f'{num} x {c} = {num*c}')
        sleep(1)
    
    cont = str(input('Deseja ver outro valor [S/N]:')).upper() .strip()
    
    if cont == 'N':
        break

print('Obrigado por testar!')