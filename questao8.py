#PROGRAMA QUE INFORMANDO O SAQUE RESPONDE QUANTAS CÉDULAS E MOEDAS DARÁ EM SUA TOTALIDADE.
saque = float(input('Informe o valor do seu saque: '))
if saque>0:
    centavos = int(saque*100)
    
    notas100 = centavos // 10000
    centavos = centavos % 10000
    if notas100>0:
        print(f'{notas100} cédula(s) de 100,00 Reais.')

    notas50 = centavos // 5000
    centavos = centavos % 5000
    if notas50>0:
        print(f'{notas50} cédula(s) de 50,00 Reais.')

    notas20 = centavos // 2000
    centavos = centavos % 2000
    if notas20>0:
        print(f'{notas20} cédula(s) de 20,00 Reais.')

    notas10 = centavos // 1000
    centavos = centavos % 1000
    if notas10>0:
        print(f'{notas10} cédula(s) de 10,00 Reais.')
    
    notas5 = centavos // 500
    centavos = centavos % 500
    if notas5>0:
        print(f'{notas5} cédula(s) de 5,00 Reais.')

    notas2 = centavos //200
    centavos = centavos % 200
    if notas2>0:
        print(f'{notas2} cédula(s) de 2,00 Reais.')

    moeda1 = centavos // 100
    centavos = centavos % 100
    if moeda1>0:
        print(f'{moeda1} moeda(s) de 1,00 Real.')

    moedas50 = centavos // 50
    centavos = centavos % 50
    if moedas50>0:
        print(f'{moedas50} moeda(s) de 50 Centavos.')

    moedas25 = centavos // 25
    centavos = centavos % 25
    if moedas25>0:
        print(f'{moedas25} moeda(s) de 25 Centavos.')

    moedas10 = centavos // 10
    centavos = centavos % 10
    if moedas10>0:
        print(f'{moedas10} moeda(s) de 10 Centavos')

    moedas5 = centavos // 5
    centavos = centavos % 5
    if moedas5>0:
        print(f'{moedas5} moeda(s) de 5 Centavos.')

    moedas01 = centavos 
    if moedas01>0:
        print(f'{moedas01} moeda(s) de 1 Centavos.')
    
else:
    print('Valor inválido.')