nome = input('Escreva seu nome completo: ')

nome_separado = nome.split()

print('Primeiro nome: {}'.format(nome_separado[0]))
print('Último nome: {}'.format(nome_separado[len(nome_separado) - 1]))