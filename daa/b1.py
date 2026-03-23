

def backtrack(index,path):
    
    if index==len(arr):
        result.append(path[:])
        return
    
    backtrack(index+1,path)

    path.append(arr[index])
    backtrack(index+1,path)
    path.pop()

    




arr = ['A','B','C']
result=[]

backtrack(0,[])

result.reverse()
print(result)









#with arr sum =k 

def backtrack(index, path, total):
    if total == target:
        result.append(path[:])
        return

    if index == len(arr) or total > target:
        return

    # exclude current element
    backtrack(index+1, path, total)

    # include current element
    path.append(arr[index])
    backtrack(index+1, path, total + arr[index])
    path.pop()


arr = [3, 4, 5, 2]
target = 7
result = []

backtrack(0, [], 0)

print(result)
