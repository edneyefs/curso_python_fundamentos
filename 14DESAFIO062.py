#Melhorar desafio 61, mostrando os 10 primeiros termos
#usando while, e o programa so encerrará quando for solicitado 0 termos
#programa que lê 10 termos de uma Progressão Aritimética
print('='*40)
print('10 TERMOS DE UMA PROGRESSÃO ARITIMÉTICA')
print('='*40)
t1 = int(input('1º termo: '))
r = int(input('Razão: '))
termo = t1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Prograssão finalizada com {} termos exibidos'.format(total))
