boardSize=5
board=[]
for i in range(boardSize):
    board.append([])
    for j in range(boardSize):
        board[i].append(0)

def _main_(board):
    xInitial=input("Input Initial X: ")
    yInitial=input("Input Initial Y: ")
    board[xInitial][yInitial]=1

def _nextPossibility_(x,y,board):
    return
def _allDirsClear_(x,y,board):
    for row in range(boardSize):#check if in same column
        if not row == y and board[row][x] ==1:
            return False
    for column in range(boardSize): #check if in same row
        if not column == x and board[y][column]==1:
            return False
    if y-1>=0: #check diagonally up and to the right and up and to the left
        for row in range(y-1,-1,-1):
            if ((x-y+row)>=0 and board[row][x-y+row]==1 )or(
                (x+y-row)<boardSize and board[row][x+y-row]==1):
                return False
    if y+1<boardSize: #check diagonally down and to the right and down and to the left
        for row in range(y+1,boardSize+1):
            if ((x-row+y)>=0 and board[row][x-row+y]==1 )or(
                (x+row-y)<boardSize and board[row][x+row-y]==1):
                return False
    return True


def test(x,y,board):
    board[y][x]=7
#    board[2][2]=1
    board[3][0]=1
    for i in range(boardSize):
        print(board[i])
    print(_allDirsClear_(x,y,board))

test(1,2,board)
