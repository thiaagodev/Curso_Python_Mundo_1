salario = float(input('Digite seu salário: '))

if salario > 1250:
    aumento = salario * 1.10
    porcent = 10
elif salario <= 1250:
    aumento = salario * 1.15
    porcent = 15

print('O aumento foi de {}%, agora seu salário é R${:.2f}'.format(porcent, aumento))
