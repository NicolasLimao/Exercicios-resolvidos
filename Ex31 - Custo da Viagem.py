distancia = int(input('Digite quantos Km será a sua viagem:'))
if distancia >= 201:
    print('Certo, sabendo que você optou para viagem mais longa...')
    print('O total a ser cobrado pela passagem é de R${} reais'.format(distancia * 0.45))
else:
    print('Como você optou pela viagem mais curta...')
    print('O total a ser cobrado pela passagem é de R${} reais'.format(distancia * 0.50))