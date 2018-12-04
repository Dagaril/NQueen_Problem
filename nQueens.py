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
    x-=1
    y-=1
    for row in range(boardSize):#check if in same column
        print(row)
        if not row == y and board[row][x] ==1:
            return False
    for column in range(boardSize): #check if in same row
        if not column == x and board[y][column]==1:
            return False
    if y+1<boardSize:
        for row in range(y+1,boardSize):
            if board[row][x-row+y]==1 or board[row][x+row-y]==1:
                return False
    if y-1>=0:
        for row in range(y-1,boardSize):
            if board[row][x-row+y]==1 or board[row][x+row-y]==1:
                return False
    return True


def test(x,y,board):
    board[2][2]=1
    board[4][4]=9
    for i in range(boardSize):
        print(board[i])
    print(_allDirsClear_(x,y,board))

test(5,5,board)
