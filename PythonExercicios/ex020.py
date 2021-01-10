import random

aluno1 = input('Digite o nome do aluno número 1: ')
aluno2 = input('Digite o nome do aluno número 2: ')
aluno3 = input('Digite o nome do aluno número 3: ')
aluno4 = input('Digite o nome do aluno número 4: ')



ordem_apresentacao = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(ordem_apresentacao)

print('A ordem de apresentação dos alunos é: {}'.format(ordem_apresentacao))