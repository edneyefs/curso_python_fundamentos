from random import randint
from time import sleep
c = randint(0,5)#faz o computador pensar
print('-=-'*20)
print('I am thinking in a number between 0 and 5. Try to guess...')
print('-=-'*20)
g = int(input('What number i am thinking? '))#faz o jogador pensar
print('Processando...')
sleep(3)
if g == c:
    print('CONGRATULATIONS! YOU WIN!')
else:
    print('YOU LOSE! I WAS THINKING {} and no {}'.format(c,g))
print('--END--')