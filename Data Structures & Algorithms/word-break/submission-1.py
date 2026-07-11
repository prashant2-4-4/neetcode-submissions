class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        def dfs(sub_str , idx):
            if idx == n:
                if sub_str in wordDict:
                    return True
                
                else:
                    return False
                

            if sub_str in memo:
                return memo[sub_str]
            

            if sub_str in wordDict:
                if dfs(s[idx] , idx+1):
                    return True
            
            if dfs(sub_str + s[idx] , idx+1):
                return True
            
            memo[sub_str] = False
            return memo[sub_str]
        
        return dfs("" , 0)
       

        