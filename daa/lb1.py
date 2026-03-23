from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr, res = [], []

        def backtrack(open_count, close_count):
        
            if open_count == close_count == n:
                res.append("".join(arr))
                return
            
            if open_count < n:
                arr.append("(")
                backtrack(open_count + 1, close_count)
                arr.pop() 
            
           
            if close_count < open_count:
                arr.append(")")
                backtrack(open_count, close_count + 1)
                arr.pop() 

        backtrack(0, 0)
        return res



  
sol = Solution()
n_input = 3

result = sol.generateParenthesis(n_input)
    
print(f"Well-formed parentheses for n={n_input}:")
print(result)