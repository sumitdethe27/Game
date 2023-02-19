import random

def printBoard():
    print(board[0], " | ", board[1], " | ", board[2])
    print("--------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("--------------")
    print(board[6], " | ", board[7], " | ", board[8],end="\n" )
    print("\n")





def player_turn(board):
    pos=int(input("enter a number between 1-9 \n"))
    if pos>=1 and pos<=9 and board[pos]=="-":
        moves.remove(pos-1)
        board[pos-1]="X"
    else:
        print("Error --Invalid input \n")



def checkwin(board,):
    global winner
    # chceck horixontal
    if board[0]==board[1]==board[2] and board[1]!='-':
        winner=True
        return True

    if board[3]==board[4]==board[5] and board[4]!='-':
        winner=True
        return True

    if board[6]==board[7]==board[8] and board[7]!='-':
        winner=True
        return True
# check vertically
    if board[0]==board[3]==board[6] and board[3]!='-':
        winner=True
        return True

    if board[1]==board[4]==board[7] and board[4]!='-':
        winner=True
        return True

    if board[2]==board[5]==board[8] and board[5]!='-':
        winner=True
        return True
#     checck diagonally
    if board[0]==board[4]==board[8] and board[4]!='-':
        winner=True
        return True

    if board[2]==board[4]==board[6] and board[6]!='-':
        winner=True
        return True
    else:
        return False
board =["-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"]


def cpu_turn(board):
    pos=random.choice(moves)
    board[pos]="O"
    moves.remove(pos)
    printBoard()



your_player="X"
cpu_player="O"
moves=[0,1,2,3,4,5,6,7,8]
printBoard()

while len(moves)!=0:
    player_turn(board)
    if checkwin(board):
        print("-----You won------")
        printBoard()
        break
    cpu_turn(board)
    if checkwin(board):
        print("------cpu won------")
        break

    if len(moves)==0:
        printBoard()
        print("Its a tie")
        break