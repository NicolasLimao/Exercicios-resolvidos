import requests 
from time import sleep
from math import ceil

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

nome = str(input('Olá, digite o seu nome:'))
print('Muito prazer Sr(a). {}'.format(nome))
sleep(1)
con = float(input('Digite quantos dolares o Sr(a). deseja converter para reais:'))
for c in range(1,3):
    print('Carregando...')
    sleep(1)
if response.status_code == 200:
    data = response.json()

    exchange_rate = data["rates"]["BRL"]
    print(f"A cotação atual do dólar para reais é: {exchange_rate}")
    sleep(1)
    conv = exchange_rate * con
    for c in range(1,3):
        print('Carregando...')
        sleep(1)
    print('A conversão será de R${} reais'. format(ceil (conv)))

else:
    print("Erro ao obter a cotação do dólar")


