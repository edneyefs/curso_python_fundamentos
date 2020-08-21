#programa que lê 10 termos de uma Progressão Aritimética
print('='*40)
print('10 TERMOS DE UMA PROGRESSÃO ARITIMÉTICA')
print('='*40)
t1 = int(input('Digite o 1º termo: '))
r = int(input('Digite a razão: '))
tf = int(input('Digite até quantos termos você quer: '))
d = t1 + (tf-1) * r
for c in range(t1,d+r, r):
    print('{}'.format(c), end=' => ')
print('ACABOU')