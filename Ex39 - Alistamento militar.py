import time
print('Olá, tudo bem ? Vamos ver se você precisa servir o Exército Brasileiro !?')
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento:'))
idade = atual - nasc
print('Sendo que você tem {} anos de idade.'.format(idade))

if idade == 18:
    print('É a hora de se alistar para o serviço militar!')
elif idade >= 19:
    print('Já passou da hora, não deve mais prestar o serviço militar')
elif idade <= 17:
    print('Ainda não está na hora, descanse mais um pouco!')
print('O exército Brasileiro agradece.')