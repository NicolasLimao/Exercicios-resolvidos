soma = 0 

print('-='*10)
print('_ Soma de varios valores _')
print('Digite qualquer número ou digite 999 para parar e somar')
print('-='*10)
while True:
    num = int(input('Digite um valor:'))
    if num == 999:
        break
    
    soma += num

print(f'A soma dos valores foi {soma}!')
