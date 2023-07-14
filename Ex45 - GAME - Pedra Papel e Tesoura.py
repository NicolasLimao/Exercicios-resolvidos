from random import randint

while True:

    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0,2)
    print('='*4,'JOKENPO','='*4)
    print('''Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
    jogador = int(input('Qual é a sua jogada?'))
    print('-='*11)
    print('Computador jogou {}'. format(itens[computador]))
    print('Jogador jogou {}'. format(itens[jogador]))
    print('-='*11)

    if computador == 0 and jogador == 0 or computador == 1 and jogador == 1 or computador == 2 and jogador == 2:
        print('Empate!')
        break
    
    elif computador == 0 and jogador == 1 or computador == 2 and jogador == 1 or computador == 2 and jogador == 0:
        print('O computador ganhou !')
        break
    
    elif computador == 1 and jogador == 0 or computador == 1 and jogador == 2 or computador == 0 and jogador == 2:
        print('O jogador ganhou !')
        break

    

