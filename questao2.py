#CALCULAR A DISTÂNCIA ENTRE DOIS PONTOS
x_a = float(input('Informe o valor de Xa: '))
y_a = float(input('Informe o valor de Ya: '))
x_b = float(input('Informe o valor de Xb: '))
y_b = float(input('Informe o valor de Yb: '))

dAB = ((x_b-x_a)**2 + (y_b-y_a)**2)**(1/2)
print(f'A distância entre os pontos ({x_a},{y_a}) e ({x_b},{y_b}) vale: {dAB:.3} ')