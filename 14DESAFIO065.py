# programa que lê vário números inteiros
# no final mostre a média entre todos os valores e qual foi o maior e o menor valores lidos
# o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores


pergunta = 'S'
soma = quantidade = media = maior = menor = 0

while pergunta in 'Ss':
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    pergunta = str(input('Quer continuar[S / N]? ')).upper()
media = soma / quantidade
print('Foram digitados {} número(s) e a média deles foi {:.2f}'.format(quantidade, media))
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
print('FIM')
