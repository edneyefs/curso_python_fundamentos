n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m >=7 <10:
    print('Aprovado, sua média é de: {}, Parabéns!'.format(m))
#if m == 10:
    #print('Aprovado, sua média foi:{}, Excelente!'.format(m))
else:
    print('Reprovado, sua média é de: {}, não desista!'.format(m))
print('---END---')
