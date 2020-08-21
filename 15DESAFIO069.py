print('-' * 19)
print('CADASTRE UMA PESSOA')
print('-' * 19)

quantidade_de_maior = quantidade_de_menor = 0
homem = mulher = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 19)
    if idade >= 18:
        quantidade_de_maior += 1
    if idade < 18:
        quantidade_de_menor += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 19)
print(f'Total de pessoas com mais de 18 anos: {quantidade_de_maior}')
print(f'Total de pessoas com menos de 18 anos: {quantidade_de_menor}')
print(f'Ao todo temos {homem} homem(ns) cadastrado(s)')
print(f'E temos {mulher} mulher(es) com menos de 20 anos')
