from time import sleep
print('\033[7;30mOlá mundo!\33[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[34m{}'.format(a, b))
n = str(input('Digite seu nome: '))
print('\033[32m ESPERE...\033[m')
sleep(3)
print('Olá, muito prazer em te conhecer, {}{}{}'. format('\033[1;33m', n.capitalize(), '\033[m]'))
