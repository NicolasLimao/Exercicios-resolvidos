from time import sleep
import math

# Banco Bauru

print('-='*20)
print('Olá! \nBem vindo a o Banco Bauru !')
print('-='*20)
sleep(1.5)
while True:
    cliente = int(input('''Se você já é cliente digite [1] 
    Se não for digite [2]'''))
    sleep(1.5)
    if cliente == 1:
        print('É muito bom ter você como cliente!')
        sleep(1.5)
        nome = str(input('Digite o seu nome:'))
        for c in range(1,3):
            print('Procurando cliente no banco de dados...')
            sleep(1.5)
        print('Já localizamos os seus dados {}! \nVamos calcular o seu Empréstimo bancário ?'.format(nome))
        sleep(1.5)
        salario = float(input('Digite o valor de sua renda mensal:'))
        casa = float(input('Digite o valor do seu imóvel:'))
        anos = int(input('Digite em quantos anos você deseja parcelar:'))
        parcela = casa / (anos * 12)
        minimo = salario * 30 / 100
        print('Para pagar uma casa de R$ {:.2f} em {} ano(s)'. format(casa, anos))
        sleep(1.5)
        print('A prestação será de R${:.2f} mensais'.format(parcela))
        sleep(1.5)
        for a in range(1,3):
            print('Calculando...')
            sleep(1.5)
        if parcela >= minimo:
            print('infelizmente como a prestação do imóvel é maior que 30% dos seus ganhos não poderemos aprovar este financiamento. ')
        elif parcela <= minimo:
            print('Muito bem como a renda do Sr(a). é de nivel elevado, o crédito do Sr(a). será aprovado dentro de 48h... \n aguarde!')
    elif cliente == 2:
        print('O Sr(a) terá que  ir até uma agencia local para a criação da conta! \n Espero ter ajudado !')
    
    else:
        print('Digite novamente o numero correto, [1] ou [2].')
        sleep(1.5)
  
