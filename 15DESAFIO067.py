while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if numero < 0:
        break
    for n in range(1, 11):
        print(f'{numero} * {n} = {n*numero}')
    print('-'*30)
print('\033[31mPrograma encerrado, volte sempre!\033[m')

# numero = int(input('Quer ver a tabuada de qual valor? '))
# while numero != 0:
#     for n in range(0, 11):
#         print(f'{numero} * {n} = {n*numero}')
#     numero = int(input('Quer ver a tabuada de qual valor? '))
# print('\033[31mPrograma encerrado, volte sempre!\033[m')
