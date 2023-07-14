from math import ceil
salario = float(input('Digite o valor do seu salario:'))
aumento = int(input('Digite o valor do aumento a ser aplicado ao salario:'))
des = salario * aumento/100
prod = salario + des
print('O valor do seu salrio é de R${} reais, com o reajuste de {}% o valor será  de R${} reais'. format(salario, aumento, ceil (prod)))