import random
from time import sleep

num = random.randint(0, 5)

print('Pensei em número, tente acertar!')
chute = int(input('Chute um número de 0 a 5: '))

print('PROCESSANDO...')
sleep(3)

if chute == num:
    print('Parabéns! você chutou {} e o número sorteado foi {}'.format(chute, num))
else: 
    print('Errado! você chutou {} e o número sorteado foi {}'.format(chute, num))