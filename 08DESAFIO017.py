from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hy = (co**2) + (ca**2)
print('O comprimento da hipotenusa é de {:.2f}'.format(sqrt(hy)))
