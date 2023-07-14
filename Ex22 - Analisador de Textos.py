nome = str(input('Digite o seu nome completo:')).strip()
print('O seu nome em letras maiusculas é {}'.format(nome.upper()))
print('O seu nome em letras minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))


