import random

aluno1 = input('Digite o nome do aluno número 1: ')
aluno2 = input('Digite o nome do aluno número 2: ')
aluno3 = input('Digite o nome do aluno número 3: ')
aluno4 = input('Digite o nome do aluno número 4: ')

lista = [aluno1, aluno2, aluno3, aluno4]

aluno_escolhido = random.choice(lista)

print('O aluno escolhido foi o {}'.format(aluno_escolhido))
