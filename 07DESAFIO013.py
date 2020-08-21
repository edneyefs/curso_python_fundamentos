n = float(input('Digite o salário do funcionário: R$'))
n1 = float(input('Digite a porcentagem da correção: '))
n2 = n1/100
n3 = n*n2
n4 = n+n3
print('O salário corrigido é de {:.2f} com a correção de {:.2f}%'.format(n4,n1))
