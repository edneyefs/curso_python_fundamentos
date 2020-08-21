print('-' * 34)
print('        LOJA SUPER BARATÃO')
print('-' * 34)

soma = quantidade = maior = menor = 0
barato = ''
caro = ''

while True:
    nome_do_produto = str(input('Nome do produto: '))
    preco_do_produto = float(input('Preço: '))
    soma += preco_do_produto
    quantidade += 1
    if quantidade == 1:
        maior = menor = preco_do_produto
        barato = caro = nome_do_produto
    else:
        if preco_do_produto > maior:
            maior = preco_do_produto
            caro = nome_do_produto
        if preco_do_produto < menor:
            menor = preco_do_produto
            barato = nome_do_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {soma:.2f} e você comprou {quantidade} produtos')
print(f'O produto mais caro foi {caro} e custou R$ {maior:.2f}')
print(f'O produto mais barato foi {barato} e custou R$ {menor:.2f}')
