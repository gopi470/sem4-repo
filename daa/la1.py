# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits)==0: return [""]

        values = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans=[""]

        for i in digits :
            temp=[]
            for j in ans:
              for k in values[i]:
                 temp.append(j+k)
              ans=temp
        
        return ans
         
sol = Solution()
print(sol.letterCombinations("23"))