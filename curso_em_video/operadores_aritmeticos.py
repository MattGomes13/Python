n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1+n2
m = n1-n2
mul = n1 * n2
pot = n1 ** n2
div = n1 / n2
divi = n1 // n2
res = n1 % n2

print('A soma é {} e a subtração é {}'.format(s, m), end='')
print('A multiplicação é {} e a potenciação é {} temos a divisão {} '.format(mul,pot,div))
print('A divisão inteira é {} e o resto é {} '.format(divi,res))
