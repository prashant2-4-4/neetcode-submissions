class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def backtrack(s , go , come):
            if go < 0 or come < 0:
                return 
            if go == 0 and come == 0:
                out.append(s)
                return 
            
            backtrack(s + '(' , go - 1 , come) 
            if go < come:
                backtrack(s + ')' , go , come-1)

            return


            
        
        backtrack("" , n , n)
        return out