from datetime import date
ano = int(input('Digite o ano de analise que deseja, ou digite 0 para analizar o ano atual: '))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano != 0 or ano % 400 == 0:

    print('O Ano de {} é Bissexto'.format(ano))

else:
    print('O Ano de {} não é Bissexto'.format(ano))
    