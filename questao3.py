#QUESTÃO 03 - PEDRA PAPEL E TESOURA
jogador_01 = str(input('Jogador 1: Escolha pedra, papel ou tesoura: ')).lower()
jogador_02 = str(input('Jogador 2: Escolha pedra, papel ou tesoura: ')).lower()
alternativas = ['pedra', 'papel', 'tesoura']

if jogador_01 == 'pedra' and jogador_02 == 'tesoura':
    print('Jogador 1 venceu.')
elif jogador_01 == 'papel' and jogador_02 == 'pedra':
    print('Jogador 1 venceu.')
elif jogador_01 == 'tesoura' and jogador_02 == 'papel':
    print('Jogador 1 venceu.')
elif jogador_01 == jogador_02:
    print('Empate.')
else:
    print('Jogador 2 venceu.')
