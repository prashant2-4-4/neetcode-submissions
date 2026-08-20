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
                
            if (idx , sub_s) in memo:
                return memo[(idx,sub_s)]
            
            if sub_s in wordDict:
                if recursion(idx+1 , s[idx]):
                    memo[(idx,sub_s)] = True
                    return memo[(idx,sub_s)]
                    # return True
            
            if recursion(idx+1 , sub_s + s[idx]):
                memo[(idx,sub_s)] = True
                return memo[(idx,sub_s)]
                # return True
            
            memo[(idx,sub_s)] = False
            return memo[(idx,sub_s)]
        
        return recursion(0 , "")

        