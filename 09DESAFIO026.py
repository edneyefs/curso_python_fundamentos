frase = str(input('Digite uma frase: ')).strip().upper()
print('Na frase tem {} letra(s) A'.format(frase.count('A')))
print('Aparece primeiramente na {}ª posição'.format(frase.find('A')+1))
print('Aparece por último na {}ª posição'.format(frase.rfind('A')+1))
