from datetime import date
from time import sleep
y = int(input('Digite o ano presente ou 0 para o ano atual: '))
print('\033[33mEspere...\033[m')
sleep(2)
if y ==0:
    y = date.today().year
if y%4==0 and y%100!=0 or y%400==0:
    print('\033[1;34m{} \033[1;32mé ano Bissexto\033[m'.format(y))
else:
    print('\033[1;34m{} \033[1;31mnão é ano Bissexto\033[m'.format(y))
