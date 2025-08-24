def print_board(parameter):
    print(parameter['top-L']+'|'+parameter['top-M']+'|'+parameter['top-R'])
    print(parameter['mid-L']+'|'+parameter['mid-M']+'|'+parameter['mid-R'])
    print(parameter['low-L']+'|'+parameter['low-M']+'|'+parameter['low-R'])


tabuleiro = {'top-L':'', 'top-M':'', 'top-R':'',
            'mid-L':'', 'mid-M':'', 'mid-R':'', 
            'low-L':'', 'low-M':'', 'low-R':''}

turn = 'X'
for i in range(9):
    print_board(tabuleiro)
    print('Rodada de '+turn+'.')
    move = input('Escolha o espaço: ')
    tabuleiro[move]=turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print_board(tabuleiro)
 