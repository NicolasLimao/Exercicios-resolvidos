from time import sleep
def caixa_eletronico(saque):
    notas = [100, 50, 10, 5, 1]
    quantidade_notas = [0, 0, 0, 0, 0]
    
    if saque < 1 or saque > 600:
        print('O valor de saque é invalido. O valor minimo é de R$ 1,00 e o maximo de R$ 600,00  ')
        return
    
    for i in range(len(notas)):
        if saque >= notas[i]:
            quantidade_notas[i] = saque // notas[i]
            saque %= notas[i]
    
    print ('Notas fornecidas:')
    for i in range (len(notas)):
        if quantidade_notas[i] > 0:
            print(f"{quantidade_notas[i]} Nota(s) de R$ {notas[i]} reais")
            sleep(1.5)

nome = str(input('qual o seu nome ? ')).strip ()
for c in range (0,2):
    print(' procurando cliente no banco de dados...')
    sleep (1.5) 

valor_saque = int(input('Sr(a) {} digite o valor de saque:'.format(nome)))
caixa_eletronico(valor_saque)
