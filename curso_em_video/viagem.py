dist = float(input('Qual a distancia da sua viagem? '))

if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45

print('O valor da viagem ficou: RS{}'.format(preco))




