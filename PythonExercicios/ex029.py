velocidade = float(input('Digite a velocidade do carro em km/h: '))

if velocidade > 80:
    valor_multa = 7 * (velocidade - 80)
    print('Você levou uma multa por velocidade excedida! terá que pagar um valor de R${}'.format(valor_multa))
else:
    print('Velocidade de acordo com os limites da pista, parabéns!')
