n1 = float(input('Digite o valor do produto: R$ '))
n2 = float(input('Qual é o desconto: '))
n3 = n2/100
n4 = (n1*n3)
n5 = n1-n4
print('Seu produto custará R${:.2f} com {:.2f}% de desconto'.format(n5,n2))
