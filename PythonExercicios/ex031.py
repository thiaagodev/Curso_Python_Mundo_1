distancia_km = float(input('Qual a distância da viagem? '))

if distancia_km <= 200:
    preco = distancia_km * 0.50
else:
    preco = distancia_km * 0.45

print('O preço da viagem é R${}'.format(preco))
