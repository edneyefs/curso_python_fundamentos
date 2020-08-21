#programa que lê vários números inteiros
#só para quando o usuário digitar 999, que é a condição de parada.
#no final, mostre quantos números foram digitados e a soma entre eles(desconsiderando o flag)
soma = 0
numero = int(input('Digite um número inteiro: '))

while numero != 999:
    numero = int(input('Digite um número inteiro: '))
    soma += 1
print(f'Foram digitados {soma} número(s)')