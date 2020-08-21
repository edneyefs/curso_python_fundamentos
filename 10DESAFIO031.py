k = float(input('Digite a distância da viagem em Km: '))
#price = k*0.50 if k<=200 else k*0.45
#print('Sua passagem terá o valor de R$ {:.2f}'.format(price))
if k <=200:
    print('Sua passagem terá o valor de R$ {:.2f}'.format(k*0.5))
else:
    print('Sua passagem terá o valor de R$ {:.2f}'.format(k*0.45))
