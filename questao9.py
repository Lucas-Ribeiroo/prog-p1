#INFORMAR O NÚMERO DE 1 À 7 E INFORMAR O DIA DA SEMANA
dia = int(input('Informe um número de 1 à 7 e veja o dia da semana correspondente: '))
if dia>=1 and dia<=7:
    if dia == 1:
        print('Domingo')
    elif dia == 2:
        print('Segunda-Feira')
    elif dia == 3:
        print('Terça-feira')
    elif dia == 4:
        print('Quarta-feira')
    elif dia == 5:
        print('Quinta-feira')
    elif dia == 6:
        print('Sexta-feira')
    elif dia == 7:
        print('Sábado')
else:
    print("Número inválido.")