#QUESTÃO 04 - CALCULAR A HIPOTENUSA DO TRIANGULO
cateto_a = float(input('Informe o valor do cateto a: '))
cateto_b = float(input('Informe o valor do cateo b: '))
produto = cateto_a**2 + cateto_b**2
hipotenusa = produto**(1/2)
print(f'A hipotenusa do triângulo vale {hipotenusa:.2f}.')