num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))
num3 = int(input('Digite outro: '))

if num1 > num2 and num1 > num3:
    print('{} é o maior número'.format(num1))
elif num2 > num1 and num2 > num3:
    print('{} é o maior numero'.format(num2))
else:
    print('{} é o maior número'.format(num3))

if num1 < num2 and num1 < num3:
    print('{} é o menor número'.format(num1))
elif num2 < num1 and num2 < num3:
    print('{} é o menor número'.format(num2))
else:
    print('{} é o menor número'.format(num3))

