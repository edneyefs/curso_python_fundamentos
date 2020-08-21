from math import radians,sin, cos, tan
n = float(input('Digite o valor do ângulo: '))
print('O seno de {} é {:.2f}\nO cosseno de {} é {:.2f}\nA tangente de {} é {:.2f}.'.format(n, sin(radians(n)), n, cos(radians(n)), n, tan(radians(n))))
