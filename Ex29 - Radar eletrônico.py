
velocidade = int(input('Digite a velocidade do carro:'))
print('Sabendo que a velocidade maxima permitida é de 80km/h, e você estava a {}'.format(velocidade))
excesso = velocidade - 80
if velocidade >= 81:
     print('Voce terá que pagar uma multa de R${} reais'.format(excesso*7))
elif velocidade <= 80:
    print('Você está dentro do limite, não terá que pagar multa!')
    