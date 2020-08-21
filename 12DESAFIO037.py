num = int(input('Digite um número inteiro: '))
input('''Qual a base de conversão?
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} ficará na forma binária {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} ficará na forma octal {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} ficará na forma hexadecimal {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida tente novamente. :D')
