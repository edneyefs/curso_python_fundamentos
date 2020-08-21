n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
c = (n1 + n2)/2
if c < 5.0:
    print('Você está REPROVADO')
    print('Sua média foi {:.1f}'.format(c))
elif c >= 5.0 and c <= 6.9:
    print('Você está de RECUPERAÇÃO')
    print('Sua média foi {:.1f}'.format(c))
elif c >= 7.0:
    print('Parabéns!! Você foi APROVADO')
    print('Sua média foi {:.1f}'.format(c))
