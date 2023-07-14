# Fahrenheit para celsius #
import math

while True:
    escolha = str(input('Digite C para Celsius e F para Fahrenheit:')).upper()
    
     # Fahrenheit para celsius #
    if escolha == ('F'):
        fah = float(input('Digite a temperatura em Fahrenheit de Bauru: '))
        calc = 5 * ((fah - 32) / 9)
        print('A temperatura atual de Bauru é de {}°C'.format(math.trunc(calc)))
        break  # Sai do loop depois de imprimir o resultado
     
     # celsius para Fahrenheit #
    elif escolha == 'C':
        cel = float(input('Digite a temperatura de Bauru em Celsius: '))
        calc2 = ((9 * cel) / 5) + 32
        print('A temperatura em Fahrenheit é de {}°F em Bauru'. format(math.trunc(calc2)))
        break  # Sai do loop depois de imprimir o resultado
    
    else:
        print('Digite novamente a letra correta, C ou F.')


