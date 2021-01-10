import math

cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))

hip2 = (cateto_oposto ** 2) + (cateto_adjacente ** 2)

print('O valor da hipotenusa é {:.2f}'.format(math.sqrt(hip2)))