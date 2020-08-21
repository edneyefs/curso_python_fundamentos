from time import sleep
print('\033[33m-=-\033[m'*15)
s = float(input('Digite o salário do funcionário: '))
print('\033[33m-=-\033[m'*15)
print('\033[36mCALCULANDO...\033[m')
sleep(3)
if s >= 1250.00:
    print('Quem ganhava R$ \033[31m{:.2f}\033[m passará a ganhar R$ \033[34m{:.2f}\033[m'.format(s, (s*0.10)+s))
else:
    print('Quem ganhava R$ \033[31m{:.2f}\033[m passará a ganhar R$ \033[34m{:.2f}\033[m'.format(s, (s*0.15)+s))
