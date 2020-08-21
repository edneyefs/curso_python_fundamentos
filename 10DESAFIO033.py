print('\033[33m-=-\033[m'*10)
n1 = int(input('Digite o primeiro número: '))
print('\033[33m-=-\033[m'*10)
n2 = int(input('Digite o segundo número: '))
print('\033[33m-=-\033[m'*10)
n3 = int(input('Digite o terceiro número: '))
print('\033[33m-=-\033[m'*10)
#verificando o menor
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#verificando o maior
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
    print('\033[33mO menor número é \033[44m{}\033[m'.format(menor))
    print('\033[33m-=-\033[m' * 10)
    print('\033[33mO maior número é \033[41m{}\033[m'.format(maior))
    print('\033[33m-=-\033[m'*10)
