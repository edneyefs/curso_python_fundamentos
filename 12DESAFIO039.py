from datetime import date
y = int(input('Ano de nascimento: '))
yt = date.today().year - y
if yt < 18:
    print('Ainda não chegou seu período de alistamento')
    print('Falta(m) {} ano(s) para você se alistar'.format(y+18-date.today().year))
    print('Você deverá se alistar no ano de {}'.format(y+18))
elif yt == 18:
    print('Você está no seu ano de alistamento')
elif yt > 18:
    print('Já passou seu ano de alistamento')
    print('Você deveria ter se alistado há {} ano(s)'.format(yt-18))
    print('Seu alistamento foi em {}'.format(y+18))