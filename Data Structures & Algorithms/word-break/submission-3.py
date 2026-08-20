class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n_s = len(s)
        memo = {}

        def recursion(idx , sub_s):
            if idx == n_s:
                if sub_s in wordDict:
                    return True
                else:
                    return False
    
            if (sub_s) in memo:
                return memo[sub_s]
            
            if sub_s in wordDict:
                if recursion(idx+1 , s[idx]):
                    memo[sub_s] = True
                    return memo[sub_s]
                    # return True
            
            if recursion(idx+1 , sub_s + s[idx]):
                memo[sub_s] = True
                return memo[sub_s]
                # return True
            
            memo[sub_s] = False
            return memo[sub_s]
        
        return recursion(0 , "")

        