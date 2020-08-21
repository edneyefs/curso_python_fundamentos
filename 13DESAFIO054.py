#programa que lê o ano de nascimento de sete pessoas
#mostra quantas pessoas são de maior e quantas são de menor
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano nasceu a {}ª pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('\033[33mAo todo tivemos {} pessoa(s) maior(es) de idade\033[m'. format(totmaior))
print('\033[32mAo todo tivemos {} pessoa(s) menor(es) de idade\033[m'. format(totmenor))
