ano = int(input('Digite um ano:'))

if ano % 4 == 0 & ano % 100 == 0 & ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
