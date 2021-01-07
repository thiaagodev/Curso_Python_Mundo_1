x = input('Digite qualquer coisa: ')

print('O tipo primitivo de "{}" é {}, é numérico: {}, é alfabético: {}, é decimal: {}, é alphanumérico: {}'.format(x, type(x), x.isnumeric(), x.isalpha(), x.isdecimal(), x.isalnum()))
