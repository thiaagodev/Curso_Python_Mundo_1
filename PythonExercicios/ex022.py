nome = input('Digite seu nome completo: ').strip()

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))

nome_separado = nome.split()

print(len(nome_separado[0]))

print(nome_separado[0], nome_separado[len(nome_separado) - 1]) # EXTRA - Imprimindo Primeiro e Ultimo Nome