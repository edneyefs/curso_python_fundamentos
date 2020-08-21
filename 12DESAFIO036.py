vc = float(input('Qual o valor da casa? '))
vs = float(input('Quanto você ganha? '))
an = int(input('Em quantos anos você quer pagar? '))
v1 = vc / (an*12)
v2 = (vs * 0.3)
print('O valor da prestação será R$ {:.2f}'.format(v1))
if v1 >= v2:
    print('Seu emprestimo foi negado pois excede 30% do seu salário.')
else:
    print('Parabéns! Seu emprestimo foi aprovado! :D')