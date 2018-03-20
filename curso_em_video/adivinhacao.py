from random import randint
cpu = randint(0,3)

dig = int(input('Qual numéro você acha que a máquina ? '))
if dig == cpu:
    print('Você acertou')
else:
    print('Você errou ')

    print('O número sortido foi: ', cpu)