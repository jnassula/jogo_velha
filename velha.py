X = "X"
O = "O"
VAZIO = " "

tabuleiro = [X, O, X,
             X, X, O,
             O, VAZIO, X]

alinhamento = False
vencedor = VAZIO

#Horizontal
for i in range(0, 9, 3):
    if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
        alinhamento = True
        vencedor = tabuleiro[i]


#Vertical
if not alinhamento:
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
            alinhamento = True
            vencedor = tabuleiro[i]
    

#Diagonal
if not alinhamento:
    for i in range(0, 3, 2):
        if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
            alinhamento = True
            vencedor = tabuleiro[i]

if alinhamento:
    print('Você venceu! ', vencedor)
else:
    if not VAZIO in tabuleiro:
        print('O jogo empatou!')
