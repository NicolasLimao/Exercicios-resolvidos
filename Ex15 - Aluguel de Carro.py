import math

dia = int(input('Digite quantos dias o carro foi alugado:'))
km = int(input('Digite a quantidade de KM que foi percorrido: '))

calc1 = dia * 60
calc2 = km * 0.15
print('O total a ser pago é de R${:.2f} reais'. format(math.ceil(calc1 + calc2)))