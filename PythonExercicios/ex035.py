print('Vou te perguntar o comprimento de 3 retas e dizer se é possível formar um triângulo')

reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a terceira reta: '))

if (reta1 + reta2) > reta3:
    print('Você pode formar um triângulo')
else:
    print('Você não pode formar um triângulo')
