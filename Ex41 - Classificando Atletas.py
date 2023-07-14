from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento:'))
idade = atual - nasc
print('Sendo que você tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('Sua categoria é Mirim.')

elif idade <= 14 and idade >= 10:
    print('Sua categoria é Infantil')

elif idade <= 19 and idade >= 15:
    print('Sua categoria é Junior')

elif idade <= 25 and idade >= 20:
    print('Sua categoria é Sênior')

elif idade >= 26:
    print('Sua categoria é Master')