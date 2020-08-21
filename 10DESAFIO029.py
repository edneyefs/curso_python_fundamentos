v = float(input('Digite a velocidade do carro: '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    print('Você deverá pagar R$ {:.2f}'.format((v-80)*7))
    #print('Tenha um bom dia! Dirija com segurança')
#else:
    #print('Você foi multado e custará R$ {:.2f}'.format((v-80)*7))