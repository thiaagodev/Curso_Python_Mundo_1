n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua média foi {}'.format(m))

if m >= 6:
    print('Sua média foi boa, parabéns!')
else: 
    print('Sua média foi ruim, estude mais!')

# print('Parabens' if m >= 6 else 'ESTUDE MAIS') - if else simplificado
