n = str(input('Qual é seu nome? '))
if n == 'Edney':
    print('Que nome bonito!')
elif n == 'Juliana' or n == 'Vera' or n == 'Jonathas':
    print ('Seu nome é legal!')
elif n == 'Mateus' or n == 'Marcos' or n == 'Lucas' or n == 'João':
    print('Seu nome é um dos evangelhos da bíblia.')
else:
    print('Seu nome é normal')
print('Tenha um bom dia {}!'.format(n.upper()))
