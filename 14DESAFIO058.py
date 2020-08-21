    #melhorar o desafio 028
    #Agora o jogador vai tentar até acertar
    #no final o computador vai dizer quantas chances ele precisou pra acertar
from random import randint
    #faz o computador pensar
computador = randint(0,10)
print('-=-'*20)
print('Acabei de pensar num número entre 0 e 10')
print('-=-'*20)
acertou = False
palpites = 0
while not acertou:
    # faz o jogador pensar
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
        print('ACERTOU MISERAVI!')
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Você precisou de {} palpite(s)'.format(palpites))
print('--END--')
