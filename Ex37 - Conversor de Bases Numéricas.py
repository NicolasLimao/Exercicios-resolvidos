from time import sleep

num = int(input('Digite um número inteiro:'))
opcao = int(input(''' Escolha uma das bases para conversão:
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal
[4] Ver todas possibilidades
'''))

for c in range(1,3):
    print('Carregando...')
    sleep(1.5)

if opcao == 1:
    print('O número {} Convertido para binário é {}'. format(num, bin(num)))
    sleep(1.5)

elif opcao == 2:
    print('O número {} Convertido para octal é {}'. format(num, oct(num)))
    sleep(1.5)

elif opcao == 3:
    print('O número {} Convertido para hexadecimal é {}'. format(num, hex(num)))
    sleep(1.5)

elif opcao == 4:
    print('''O numero {}: 
    Convertido para binario: {} 
    Convertido para octal: {}
    Convertido para hexadecimal: {}'''.format(num,bin(num), oct(num), hex(num)))
    sleep(1.5)