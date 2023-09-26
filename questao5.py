#QUESTÃO 05 - LEIO O ANGULO E INFORME O TIPO DO TRIANGULO (FEITO)
angulo = float(input('Informe o ângulo do triangulo: '))
if angulo<=180 and angulo>=0:
    if angulo < 90:
        print('O triângulo é do tipo acutângulo.')
    elif angulo == 90:
        print('O triângulo é do tipo retângulo.')
    else:
        print('O triângulo é do tipo obtusângulo.')
else:
    print('Angulo inválido.')