tot18 = toth = totm20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')) .strip() .upper() [0]
    
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Digite [C/P] para continuar ou parar: ')).strip() .upper() [0]

    if resp == 'P':
        break

print(f'O total de pessoas com mais de 18 anos é de {tot18}.')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totm20} mulher(es) com menos de 20 anos.')
