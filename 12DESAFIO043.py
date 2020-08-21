from time import sleep
w = float(input('Digite seu peso [Kg]: '))
h = float(input('Digite sua altura [m]: '))
imc = w / (h**2)
print('\033[33mCalculando...\033[m')
sleep(2)
print('\033[33m -=-\033[m'*5)
print('Seu IMC é de \033[33m{:.2f}\033[m'.format(imc))
print('\033[33m -=-\033[m'*5)
if imc <= 16.99:
    print('''\033[35mMUITO ABAIXO DO PESO\033[m
Efeitos: Queda de cabelo, infertilidade, ausência menstrual''')
elif 17 < imc <= 18.49:
    print('''\033[31mABAIXO DO PESO\033[m
Efeitos: Fadiga, stress, ansiedade''')
elif 18.5 < imc <= 24.99:
    print('''\033[32mPESO NORMAL\033[m
Efeitos: Menor risco de doenças cardíacas e vasculares''')
elif 25 < imc <= 29.99:
    print('''\033[31mACIMA DO PESO\033[m
Efeitos: Fadiga, má circulação, varizes''')
elif 30 < imc <= 34.99:
    print('''\033[31mOBESIDADE GRAU I\033[m
Efeitos: Diabetes, angina, infarto, aterosclerose''')
elif 35 < imc <= 40:
    print('''\033[35mOBESIDADE GRAU II\033[m
Efeitos: Apneia do sono, falta de ar''')
elif imc > 40:
    print('''\033[35mOBESIDADE GRAU III\033[m
Efeitos: Refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC''')
