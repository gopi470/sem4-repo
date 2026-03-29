def safe(row,col,board):
    dupcol,duprow=col,row

    while(row>=0 and col>=0):
        if(board[row][col]=='Q') :return False
        row-=1
        col-=1
    
    row,col=duprow,dupcol
    while( col>=0):
        if(board[row][col]=='Q') :return False
        col-=1
        
    row,col=duprow,dupcol
    while( col>=0 and row<n):
        if(board[row][col]=='Q') :return False
        row+=1
        col-=1

    return True


def backtrack(col):

    if(col==n):
        res.append([" ".join(row) for row in board])
        return
    
    for row in range (n):
        if(safe(row,col,board)):
            board[row][col]='Q'
            backtrack(col+1)
            board[row][col]='.'




n=4
board=[['.' for _ in range(n)] for _ in range(n)]
res=[]


backtrack(0)

for i in res:
    for j in i:
        print(j)
    print("\n")