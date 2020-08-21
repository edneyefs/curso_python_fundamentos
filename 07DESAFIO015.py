km = float(input('Km rodada: '))
d = int(input('Digite quantos dias de aluguel: '))
c1 = (km * 0.15) + (d * 60)
print('O total a ser pago é de R${:.2f}'.format(c1))
