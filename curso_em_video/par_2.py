from random import randint
num = float(input('Digite o número de 0 a 3 ver se acerta o que a máquina pensa '))
cpu = randint(0,3)
if num == cpu:
    print('Você acertou!')
else:
    print('Você errou, a cpu escolheu o número {}'.format(cpu))