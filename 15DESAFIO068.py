from random import randint
contador = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    jogador = int(input('Diga um valor? '))
    computador = randint(0, 11)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Par ou Ímpar? [Pp/Ii]')).strip().upper()
    if escolha == 'P':
        if total % 2 == 0:
            print('Você ganhou!!')
            print(f'Você jogou {jogador} e o computador {computador} = {total}')
            contador += 1
        else:
            print('Você PERDEU!')
            print(f'Você jogou {jogador} e o computador {computador} = {total}')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você ganhou!!')
            print(f'Você jogou {jogador} e o computador {computador} = {total}')
            contador += 1
        else:
            print('Você PERDEU!')
            print(f'Você jogou {jogador} e o computador {computador} = {total}')
            break
    print('Vamos jogar novamente...')
print(f'Você ganhou {contador} vez(es)')
print('Fim')

# from random import randint
# contador = 0
# print('=-'*20)
# print('VAMOS JOGAR PAR OU ÍMPAR')
# print('=-'*20)
# while True:
#     jogador = int(input('Diga um valor? '))
#     computador = randint(0, 11)
#     escolha = str(input('Par ou Ímpar? [P/I]')).upper()
#     if escolha == 'P' and (jogador + computador) % 2 == 0:
#         print('Você ganhou!!')
#         print(f'Você jogou {jogador} e o computador {computador} = {jogador + computador}')
#         print('Vamos jogar novamente')
#         contador += 1
#     elif escolha == 'I' and (jogador + computador) % 3 == 0:
#         print('Você ganhou!!')
#         print(f'Você jogou {jogador} e o computador {computador} = {jogador + computador}')
#         print('Vamos jogar novamente')
#         contador += 1
#     else:
#         print(f'Você jogou {jogador} e o computador {computador} = {jogador + computador}')
#         print('Você perdeu!')
#         break
# print(f'Você ganhou {contador} vez(es)')
# print('Fim')
