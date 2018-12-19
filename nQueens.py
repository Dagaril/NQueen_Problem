boardSize=15
def _init_():
    board=[]
    for i in range(boardSize):
        board.append([])
        for j in range(boardSize):
            board[i].append(0)
    return board

def _main_(board):
    xInitial=int(input("Input Initial X: "))
    yInitial=int(input("Input Initial Y: "))
    board[yInitial][xInitial]=1
    _nextPossibility_(xInitial,yInitial,board)
    for i in range(boardSize):
        print(board[i])
    print(_verifyBoard_(board))

        
def _testerMain_(x,y,board):
    board[y][x]=1
    _nextPossibility_(x,y,board)

def _nextPossibility_(x,y,board):
    x+=1
    if(x==boardSize):
        x=0
    if(_findSumBoard_(board)==boardSize):
        return
    for yNew in range(0,boardSize):
        if _allDirsClear_(x,yNew,board):
            board[yNew][x]=1
            y=yNew
            ret=_nextPossibility_(x,y,board)
            if(ret!=None):
                board[yNew][x]=0
    if(_findSumCol_(x,board)==0):
        return "dead"
    return

def _findSumBoard_(board):
    total=0
    for i in range(boardSize):
        for j in range(boardSize):
            total+=board[i][j]
    return total

def _findSumCol_(col,board):
    total=0
    for i in range(boardSize):
           total+=board[i][col]
    return total

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
        for row in range(y+1,boardSize):
            if ((x-row+y)>=0 and board[row][x-row+y]==1 )or(
                (x+row-y)<boardSize and board[row][x+row-y]==1):
                return False
    return True

def _verifyBoard_(board): #prints True if queen layout is valid
    for i in range(boardSize):
        for j in range(boardSize):
            if not board[i][j]==1 and _allDirsClear_(j,i,board):
                return False
    return True

board=_init_()
'''
num=0
for i in range(boardSize):
    for j in range(boardSize):
        num+=1
        _testerMain_(i,j,board)
        print(_verifyBoard_(board),num)
        board=_init_()
'''
_main_(board)
