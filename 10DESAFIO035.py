print('\033[33m -=-\033[m'*20)
print('\033[32mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[33m -=-\033[m'*20)
a = float(input('Digite o comprimento[cm] do lado A do triângulo: '))
print('\033[33m -=-\033[m'*20)
b = float(input('Digite o comprimento[cm] do lado B do triângulo: '))
print('\033[33m -=-\033[m'*20)
c = float(input('Digite o comprimento[cm] do lado C do triângulo: '))
print('\033[33m -=-\033[m'*20)
if a < b + c and b < a+c and c < a+b:
    print('Os lados A B C \033[34mPODEM\033[m formar um triângulo')
else:
    print('Os lados A B C \033[31mNÃO PODEM\033[m formar um triângulo')
