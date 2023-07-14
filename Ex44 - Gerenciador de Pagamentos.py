from time import sleep




print('='*6, 'Lojas Bauru', '='*6)

valor = float(input('''Checking - Digite o valor de compra:'''))

while True:
    
    print(''' Formas de pagamento:
    [1] A vista no Dinheiro ou PIX (10% de desconto)
    [2] Cartão de Débito
    [3] Cartão de Crédito (sem juros)''')

    pagamento = int(input('Digite qual opção deseja:'))
    for f in range(1,3):
      print('Carregando...')
      sleep(1.2)
 
    if pagamento == 1:
     desconto = valor - (valor * 10 / 100)
     print('O Valor a ser pago é de R${:.2f} reais com 10% de desconto.'. format(desconto))
     break
 
    elif pagamento == 2:
     print('='*3,'Mastercard - Crédito','='*3)
     print('O Valor a ser pago é de R${:.2f} reais.'. format(valor))
     for d in range(1,4):
      print('Carregando...')
      sleep(1.2)
     while True:
       senha = int(input('Digite a senha para compra no débito:'))
       if senha == 1234:
        print('Senha correta!')
        for a in range(1,3):
         print('Carregando...')
         sleep(1)
         print('Pagamento confirmado, valor de R$ {}'.format(valor))
         break
    
        else:
           print('Senha incorreta, digite novamente!')
           
           

    elif pagamento == 3:
      print('='*3,'Mastercard - Crédito','='*3)
      print('''
            [1] 1x de {:.2f}
            [2] 2x de {:.2f}
            [3] 3x de {:.2f}
            [4] 4x de {:.2f}
            [5] 5x de {:.2f}
            [6] 6x de {:.2f}'''.format((valor),(valor / 2),(valor / 3),(valor / 4),(valor / 5),(valor / 6)))
      parcela = int(input('Digite quantas parcelas você deseja: '))
      for d in range(1,4):
       print('Carregando...')
       sleep(1.2)
      senha = int(input('Digite a senha para compra no crédito:'))
      while True:
       if senha == 1478:
        print('Senha correta!')
        print('Pagamento confirmado, valor de R$ {}'.format(valor))
  
       else:
         print('Senha incorreta, digite novamente!')
       break
    else:
     print('Digite as opções de [1] a [3]')
     sleep(1)
     for d in range (1,3):
       print('recarregando...')
       sleep(1.2)