import math
print('Vamos calcular o seu IMC ?')
nome = str(input('Digite o seu nome ?'))
peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
imc = peso / (altura*altura)
if imc <= 18.5:
    print('{}, de acordo com o seu peso {}Kg e sua altura {}m, seu IMC é igual a {} \n logo você está abaixo do peso'.format(nome,peso,altura,math.ceil(imc)))
elif imc >= 18.5 and imc <= 25:
    print('{}, de acordo com o seu peso {}Kg e sua altura {}m, seu IMC é igual a {} \n logo você está com o peso ideal'.format(nome,peso,altura,math.ceil(imc)))
elif imc >= 25 and imc <= 30:
    print('{}, de acordo com o seu peso {}Kg e sua altura {}m, seu IMC é igual a {} \n logo você está com sobrepeso'.format(nome,peso,altura,math.ceil(imc)))
elif imc >= 30 and imc <= 40:
    print('{}, de acordo com o seu peso {}Kg e sua altura {}m, seu IMC é igual a {} \n logo você está obeso'.format(nome,peso,altura,math.ceil(imc)))
elif imc >= 40:
    print('{}, de acordo com o seu peso {}Kg e sua altura {}m, seu IMC é igual a {} \n logo você está obeso morbito, procure um médico!'.format(nome,peso,altura,math.ceil(imc)))
