n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite um número qualquer: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1,n2))
elif n1 < n2:
    print('{} é maior que {}'.format(n2,n1))
elif n1 == n2:
    print('Não existe valor maior, {} é igual a {}'.format(n1,n2))
