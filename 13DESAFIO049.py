#programa que lê um número e dá sua tabuada
n = int(input('Digite um número pra ver sua tabuada: '))
print('A tabuada de {}'.format(n))
for c in range(0,11):
    print('{} x {} = {}'.format(n,c,n*c))
