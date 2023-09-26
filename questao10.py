#APROVAR O RECUSAR O EMPRÉSTIMO DE ACORDO COM A PORCENTAGEM BASEADA NO SALÁRIO
salario = float(input('Informe o valor do seu sálario: '))
emprestimo = float(input('Informe o valor desejado para o empréstimo: '))
if emprestimo > salario*20/100:
    print('Emprestimo negado.')
else:
    print('Empréstimo concedido.')