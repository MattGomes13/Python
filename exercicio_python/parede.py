largura = float(input('Digite a largura da parede: '))
comprimento = float(input('Digite o comprimento da parede: '))
area = largura * comprimento
tinta = area / 2

print('Sua parede tem a dimensao de {} x {} e sua área é {}². \n para pintar essa parede será necessário {}Ls de tinta'.format(largura,comprimento,area,tinta))