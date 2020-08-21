#programa que lê um número inteiro
#e diz se é primo ou não
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('O número {} é \33[33mPRIMO\33[m.'.format(n))
else:
    print('O número {} \33[31mNÃO É PRIMO\33[m'. format(n))
