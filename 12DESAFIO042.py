print('\033[33m -=-\033[m'*13)
print('\033[32mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[33m -=-\033[m'*13)
a = float(input('Digite o comprimento[cm] do lado A do triângulo: '))
print('\033[33m -=-\033[m'*13)
b = float(input('Digite o comprimento[cm] do lado B do triângulo: '))
print('\033[33m -=-\033[m'*13)
c = float(input('Digite o comprimento[cm] do lado C do triângulo: '))
print('\033[33m -=-\033[m'*13)
if a < b + c and b < a+c and c < a+b:
    print('Os lados A B C \033[34mPODEM\033[m formar um triângulo')
    if a == b == c:
        print('O triângulo é EQUILÁTERO = todos os lados iguais')
    elif a != b != c != a:
        print('O triângulo é ESCALENO = todos os lados diferentes')
    else:
        print('O triângulo é ISÓSCELES = dois lados iguais')
else:
    print('Os lados A B C \033[31mNÃO PODEM\033[m formar um triângulo')
