total = totmil = menor = cont = 0
barato = ' '

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$: '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    
    if cont == 1 or preço < menor: 
        menor = preço
        barato = produto
            
    resp = '  '
    
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')) .strip() .upper() [0]
    
    if resp == 'N':
        break

print('{:-^40}'. format(' Fim do programa '))
print(f'O total da compra foi de R$ {total:.2f} reais.')
print(f'{totmil} produto(s) custou mais de R$ 1.000,00 reais')
print(f'O produto mais barato é {barato} que custa R$ {menor:.2f} reais.')