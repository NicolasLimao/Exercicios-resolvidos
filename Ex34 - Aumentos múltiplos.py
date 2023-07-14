from time import sleep

salario = float(input('Digite o seu salario atual para calcularmos o seu aumento:'))
for c in range(1,3):
    print('Calculando...')
    sleep(1.3)
if salario <= 1250.00:
    print('Muito bem, como o salario do Sr(a), é de {} e o rajuste será de 10%'.format(salario))
    print('O Seu novo salario é de {:.2f}'. format(salario + (salario * 0.10)))
    
if salario >= 1251.00:
    print('Muito bem como o salario do Sr(a), é de {} e o reajuste será de 15%'. format(salario))
    print('O Seu novo salario é de {:.2f}'. format(salario + (salario * 0.15)))
    