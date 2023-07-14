import math
preço_lata = 80
tamanho_lata = 18
area = float(input('Quantos metros quadrados serão pintados ?'))
litros_tinta = area / 3
quantidade_latas = math.ceil(litros_tinta / tamanho_lata)
preço_total = quantidade_latas * preço_lata
print('Você precisará de, {} latas de tinta'.format (quantidade_latas))
print('O valor total a ser gasto é de R${} reais'.format(preço_total))