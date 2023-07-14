frase = str(input('Digite uma frase:')).strip().upper()
palravas = frase.split()
junto = ''.join(palravas)
inverso = ''
for letra in range (len(junto)- 1, - 1, -1):
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print('A frase é um palíndromo!')

else:
    print('A frase não é um palíndromo!')
    