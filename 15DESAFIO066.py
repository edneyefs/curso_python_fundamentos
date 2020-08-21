soma = quantidade = 0

while True:
    numero = int(input('Digite um número (condição de parada 999): '))
    if numero == 999:
        break
    soma += numero
    quantidade += 1
print(f'A soma dos {quantidade} número(s) é {soma}')
