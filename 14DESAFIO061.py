#Melhorar desafio 51, mostrando os 10 primeiros termos
#usando while
#programa que lê 10 termos de uma Progressão Aritimética
print('='*40)
print('10 TERMOS DE UMA PROGRESSÃO ARITIMÉTICA')
print('='*40)
primeiro = int(input('1º termo: '))
r = int(input('Razão: '))
termo = primeiro
cont = 1
#tf = 10
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')
