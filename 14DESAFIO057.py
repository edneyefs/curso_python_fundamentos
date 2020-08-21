#programa que lê o sexo de uma pessoa
#aceitando somente M / F
#caso não seja peça que digite novamente até que esteja correto
sexo = str(input('Digite seu sexo [M / F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo [M / F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


#sexo = str(input('Digite seu sexo [M / F]: ')).strip().upper()[0]
#while r == 'S':
#    if sexo =! 'M' or 'F':
#        if s == 'M':
#            m += 1
#        if s == 'F':
#            f += 1
#    s = str(input('Digite seu sexo [M / F]: ')).upper()
#    r = str(input('Quer continuar? ')).upper()
#print('Foram contabilizado(s) {} homem(ns) e {} mulher(es)'.format(m, f))