from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('\033[33m -=- \033[m'*6)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('\033[33m -=- \033[m'*6)
if computador == 0:
    if jogador == 0:
        print('Deu empate!')
    elif jogador == 1:
        print('Parabéns!! Você venceu! :D')
    elif jogador == 2:
        print('Que pena, você perdeu :´(')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('Que pena, você perdeu :´(')
    elif jogador == 1:
        print('Deu empate!')
    elif jogador == 2:
        print('Parabéns!! Você venceu! :D')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('Parabéns!! Você venceu! :D')
    elif jogador == 1:
        print('Que pena, você perdeu :´(')
    elif jogador == 2:
        print('Deu empate!')
    else:
        print('JOGADA INVÁLIDA')