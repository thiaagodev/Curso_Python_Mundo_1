preco_produto = float(input('Informe o preço do produto: '))

preco_desconto = preco_produto - (preco_produto * 0.05)

print('O novo preço do produto com 5% de desconto é R${}'.format(preco_desconto))
