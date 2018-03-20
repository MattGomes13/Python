vel = float(input('Qual velocidade você estava?: '))
if vel > 80:
    multa = (vel - 80) * 7

    print('Sua multa é de {}'.format(multa))

else:
    print('Tenha um bom dia e diriga com cuidado')