#programa que lê um número inteiro e mostre na tela
#os n primeiros números de uma sequência de Fivonacci
#Ex: 0.1.1.2.3.5.8
print('-'*22)
print('\033[32mSEQUÊNCIA DE FIBONACCI\033[m')
print('-'*22)

quantidade = int(input('Quantos termos você quer mostrar? '))

def fibonnaci(quatidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado

if __name__ == '__main__':
    for fib in fibonnaci(quantidade):
        print(f'{fib}', end=' ')