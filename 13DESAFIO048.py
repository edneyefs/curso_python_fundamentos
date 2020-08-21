#programa que calcula a soma
#entre todos os números impares
#que são múltiplos de 3 e que se encontram
#no intervalo de 1 até 500
n1 = int(input('Digite o número que começa o intervalo: '))
n2 = int(input('Digite o número que finaliza o intervalo: '))
n3 = int(input('Digite o número de casa que quer pular: '))
n4 = int(input('Digite o número múltiplo que deseja o somatório: '))
soma = 0
cont = 0
for c in range(n1, n2, n3):
    #condição para número múltiplo de 3
    if c % n4 == 0:
        soma += c
        cont += 1
print('o soma de todos os {} valores solicitados é {}'.format(cont, soma), end=' ')

#s = 0
#for c in range(1, 501, 2):
    #condição para número múltiplo de 3
    #if c % 3 == 0:
    #    s+= c
#print('o somatório dos valores solicitados é igual a {}'.format(s), end=' ')
