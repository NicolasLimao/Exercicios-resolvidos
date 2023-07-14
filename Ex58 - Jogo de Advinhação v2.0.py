from random import randint

computador = randint(0,10)

print('Olá humano !... está pronto para perder no jogo de advinhação ?')
while True:
    escolha = str(input('[SIM] ou [NÃO]:')).strip() .lower()
    
    if escolha == 'sim':
        print('Muito bem! vamos lá !')
        
        print('Acabei de pensar em um numero de 0 a 10!')
        acertou = False
        palpite = 0
        while not acertou:
            jogador = int(input('Digite o seu palpite:'))
            palpite += 1
            if jogador == computador:
                acertou = True
            
            else: 
                if jogador < computador:
                    print('O numero é maior... tente mais uma vez.')
                elif jogador > computador:
                    print('O numero é menor... tente mais uma vez.')
        print('Você acertou com {} tentativas ! realmente eu estava pensando no numero {}'.format(palpite, jogador))
        break 

    if escolha == 'nao':
        print('Você não teria chance mesmo !')
        break
    
    else:
        print('Escolha entre [SIM] e [NÃO]')       