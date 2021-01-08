n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisao é {:.3f}'.format(s, m, d), end = ' >>>>>> ')
print('Divisão inteira é {} \n Potência é {}'.format(di, e))
