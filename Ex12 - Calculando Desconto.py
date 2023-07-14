from math import ceil
produto = float(input('Digite o valor do produto:'))
desconto = int(input('Digite o valor do desconto a ser aplicado:'))
des = produto * desconto/100
prod = produto - des
print('O valor do produto é de R${} reais, com o reajuste de {}% o valor será R${} reais'. format(produto, desconto, ceil (prod)))