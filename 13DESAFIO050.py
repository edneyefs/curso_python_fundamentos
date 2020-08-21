#programa que lê seis números e mostra a soma somente dos pares
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    #condição para o número ser par ou mutiplo de dois
    if n%2 == 0:
        soma += n
        cont += 1
print('Você informou {} pares e a soma deles é {}.'.format(cont, soma))
