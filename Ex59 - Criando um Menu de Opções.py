from time import sleep

valor1 = float(input('Digite o primeiro valor: '))
sleep(1)
valor2 = float(input('Digite o segundo valor: '))
sleep(1)

opção = 0
while opção != 5:
    print('-=-'*4, 'Menu de Opções', '-=-'*4)
    print('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior e Menor
    [4] - Novos numeros
    [5] - Sair do programa
    ''')
    opção = int(input('Digite a sua escolha de [1] a [5]:  '))
    sleep(1)
    if opção == 1:
        print('A soma entre {} e {} é {}'.format(valor1, valor2, (valor1 + valor2)))
        sleep(1)
        break
    
    elif opção == 2:
        print('A multiplicação entre {} e {} é {}'. format(valor1, valor2, (valor1 * valor2)))       
        sleep(1)
        break
        
    elif opção == 3:
        if valor1 > valor2:
            print('O maior valor é {}'.format(valor1))
        else:
            print('O maior valor é {}'. format(valor2))    
        break
    
    elif opção == 4:
        print('Digite os novos valores')
        valor1 = float(input('Digite o primeiro valor: '))
        sleep(1)
        valor2 = float(input('Digite o segundo valor: '))
        sleep(1)
        
    elif opção == 5:
        for c in range(1,4):
            print('Finalizando...')
            sleep(1.2)
        
    else:
        print('opção inválida. tente novamente')
    
    print('-=-' * 10)

print('Fim do programa!')                


    
