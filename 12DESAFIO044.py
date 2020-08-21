v = float(input('Valor do produto \33[31m[R$]\33[m: '))
print('''Qual a forma de pagamento?
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Sua opção: '))
if op == 1:
    t = v - (v * 0.1)
elif op == 2:
    t = v - (v * 0.05)
elif op == 3:
    t = v
    p1 = t /2
    print('Sua compra parcelada em 2x de R$ {:.2f} SEM JUROS'.format(p1))
elif op == 4:
    t = v + (v * 0.2)
    tp = int(input('Quantas parcelas: '))
    vp = t / tp
    print('Sua compta será parcelada em {}x de R$ {:.2f} COM JUROS'.format(tp, vp))
else:
    t = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(v, t))
