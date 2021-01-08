numero = int(input('Informe um número inteiro: '))

print('A tabuada de {} é: '.format(numero))
for i in range(1, 11, 1):
    print('{} x {} = {}'.format(numero, i, numero * i))
