print('-='*15)
print('° Analisador de Triângulos °')
print('-='*15)
r1 = int(input('Digite a primeira reta:'))
r2 = int(input('Digite a segunda reta:'))
r3 = int(input('Digite a terceira reta:'))

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
    if r1 == r2 == r3:
        print('Triangulo Equlátero!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Triangulo isósceles')
    elif r1 != r2 != r3:
        print('Triangulo escaleno')
        
else:
    print('Os segmentos acima não podem formar um triângulo!')


    
    