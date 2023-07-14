resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'S':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    
    resp = str(input('Deseja continuar digite [S/N]: ')).strip() .upper()
media = soma / num
print(f'Você digitou {quant} números e a mèdia foi de {media:.2f}')
print('Acabou!')