#programa que lê uma frase
#e diga se ela é um palíndromo(mesma escrita de traz pra frente)
#desconsiderando os espaços e acentos
#Ex: apos a sopa;
#a sacada da casa;
#a torre da derrota;
#o lobo amo o bolo;
#anotaram a data da maratona
f = str(input('Digite sua frase: ')).strip().upper()
#dividindo em palavras
w = f.split()
#retirando os espaços entre as palavras
t = ''.join(w)
#invertendo a frase
#i = t[::-1]
i = ''
for l in range (len(t) -1, -1, -1):
    i += t[l]
#print()
print('O inverso de {} é {}.'.format(t, i))
if i == t:
    print('A frase que você digitou é um \033[32mPALÍNDRIMO\033[m.')
else:
    print('A frase que você digitou \033[31mNÃO É UM PALÍNDRIMO\033[m.')
