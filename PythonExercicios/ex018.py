import math

angulo = float(input('Digite um ângulo qualquer: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('Ângulo: {} | seno: {} | cosseno: {} | tangente: {}'.format(angulo, sen, cos, tang))
