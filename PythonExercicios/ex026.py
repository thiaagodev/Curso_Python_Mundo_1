frase = input('Digite uma frase: ')


print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')))