dias_alugados = int(input('Quantos dias o carro foi alugado? '))
km_rodados = float(input('Quantos Km foram rodados? '))

total_a_pagar = (dias_alugados * 60) + (km_rodados * 0.15)

print('O total a pagar é de R${:.2f}'.format(total_a_pagar))