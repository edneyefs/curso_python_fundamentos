#programa que lê o nome, idade e sexo de 4 pessoas
#mostra a idade média do grupo
#qual o nome do homem mais velho
#quantas mulheres tem menos de 20 anos
tidade = 0
midade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    tidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
midade = tidade / 4
print('A média de idade do grupo é de {} anos.'.format(midade))
print('O nome do homem mais velho é {}, e ele tem {} anos.'.format(nomevelho, maioridadehomem))
print('No grupo tem {} mulher(es) com menos de 20 anos'.format(totmulher20))
