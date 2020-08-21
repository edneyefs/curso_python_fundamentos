n1 = float(input('Digite a largura [m]:'))
n2 = float(input('Digite a altura [m]:'))
n3 = n1*n2
n4 = float(input('digite o rendimento de sua tinta [l]:'))
n5 = n3/n4
print('Sua área é de {:.2f} m², sendo necessário {:.1f} l de tinta'.format(n3,n5))
