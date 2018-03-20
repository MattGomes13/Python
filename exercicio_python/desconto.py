valor = float(input('Digite o valor do produto: '))
desc = valor - (valor * 5/100)


print('O valor original é R${} com o desconto de 5% fica R${}'.format(valor,desc))
