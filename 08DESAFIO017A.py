from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é de {:.2f}'.format(hypot(co, ca)))
