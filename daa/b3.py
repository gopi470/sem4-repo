
def backtrack(r,c,i):

    if i==len(word):
        return True
    
    if(r<0 or c<0 or r>=n_r or c>=n_c or word[i]!=grid[r][c]  or (r,c) in path):
        return False
    

    path.add((r,c))
    res=(backtrack(r-1,c,i+1) or backtrack(r+1,c,i+1)  or backtrack(r,c-1,i+1)  or backtrack(r,c+1,i+1) )
    path.remove((r,c))
    return res


def solution():
    
    for r in range (n_r):
        for c in range (n_c):
          if backtrack(r,c,0): return True

    return False


m = 3 # Rows
n = 4 # Columns



n_r,n_c=m,n

grid = [[" " for _ in range(n)] for _ in range(m)]
path=set()

for i in range(m):
    for j in range(n):
        grid[i][j] = input()

word=input("Enter the word :")

print()
for i in range(m):
    for j in range(n):
        print(grid[i][j], end=" ")
    print() 




print(f"Found : {solution()}")






