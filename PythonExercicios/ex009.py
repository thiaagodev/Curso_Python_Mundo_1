numero = int(input('Informe um número inteiro: '))

print('A tabuada de {} é: '.format(numero))

print('-' * 11)

for i in range(1, 11, 1):
    print('{} x {:2} = {}'.format(numero, i, numero * i))

print('-' * 11)