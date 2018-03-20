casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário?'))
parcela = int(input('Em quantas parcelas gostaria de fazer? '))

par_mensal = casa / parcela
if par_mensal > (salario * 30) /100:
    print('Empréstimo negado, o valor das parcelas ultrapassa 30% do seu salário')
else:
 print('O valor das parcelas será de R${} reais por {} meses'.format(par_mensal,parcela))
