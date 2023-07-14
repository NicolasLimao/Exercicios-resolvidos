while True:
    
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
    if sexo == 'M':
        print('Você é homem!')
        break
    
    if sexo == 'F':
        print('Você é mulher!')
        break
    
    else: 
        print('Digite novamente [M] ou [F] !')
        
    