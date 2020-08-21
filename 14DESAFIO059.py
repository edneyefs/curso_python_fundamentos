#programa que leia dois valores e mostre um menu
# (1+) (2*) (3<) (4novos números) (5sair do programa)
#o programa deve realizar o solicitado pelo usuário
from time import sleep
n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
op = 0
while op != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    op = int(input('Qual sua opção: '))
    if op == 1:
        s = n1 + n2
        print('{} + {} = {}'.format(n1, n2, s))
    elif op == 2:
        p = n1 * n2
        print('{} * {} = {}'.format(n1, n2, p))
    elif op == 3:
        if n1 > n2:
            print('{} > {}'.format(n1,n2))
        else:
            print('{} < {}'.format(n1, n2))
    elif op == 4:
        n1 = int(input('1º valor: '))
        n2 = int(input('2º valor: '))
    elif op == 5:
        print('OBRIGADO')
    else:
        print('\33[31mOpção inválida! Tente novamente!\33[m')
    print('\33[33m=-=\33[m'*10)
    sleep(2)
print('Fim do programa! Volte sempre!')
