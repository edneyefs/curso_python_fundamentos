print('=' * 30)
print('{:^30}'.format('BANCO EDY'))
print('=' * 30)
saque = int(input('Quanto você quer sacar? R$ '))
total = saque
cedula = 50
quantidade_cedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        quantidade_cedulas += 1
    else:
        if quantidade_cedulas > 0:
            print(f'Total de {quantidade_cedulas} de R$ {cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        quantidade_cedulas = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO EDY! Tenha um bom dia!')
