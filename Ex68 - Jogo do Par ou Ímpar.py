from random import randint

v = 0

while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PAR''IMPAR':
        tipo = str(input('DIgite a sua escolha [Par / Impar]')).strip() .upper()
    print(f'Você jogou {jogador} e o computador {computador}. Um total de {total}')

    if tipo == 'PAR':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'IMPAR':
        if total % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu, mais sorte da próxima vez!')
            break
    
    print('Vamos jogar novamente!')

if v >= 2:
    print(f'Game over!. Você venceu {v} vezes!')

elif v == 1:
    print(f'Game over!. Você venceu {v} unica vez!')

elif v == 0:
    print('K.O você não teve chance contra a maquina!')