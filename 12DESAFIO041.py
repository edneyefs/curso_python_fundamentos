from datetime import date
y = int(input('Ano de nascimento: '))
yt = date.today().year - y
if yt <= 9:
    print('Sua categoria é MIRIM')
elif 9 < yt <= 14:
    print('Sua categoria é INFANTIL')
elif 14 < yt <= 19:
    print('Sua categoria é JUNIOR')
elif 19 < yt <= 20:
    print('Sua categoria é SÊNIOR')
elif yt > 20:
    print('Sua categoria é MASTER')