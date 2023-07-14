#Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maiores = 0
for c in range(1,8):
    idade = int(date.today().year - int(input('Digite o {}° ano de nascimento: '.format(c))))
    if idade >= 18:
        maiores += 1
print('Entre essas 7 pessoas existem {} maiores e {} menores.'.format(maiores, 7 - maiores))