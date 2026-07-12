class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n1 , n2 = len(text1) , len(text2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(1 , n1+1):
            for j in range(1 , n2+1):

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        return dp[-1][-1]


        # sub_text1 = set()
        # sub_text2 = set()
        # n1 = len(text1)
        # def dfs1(idx , sub_str):
        #     sub_text1.add(sub_str)
        #     if idx == n1:
        #         return 

        #     # if sub_str in sub_text1:
        #     #     return 
        

        #     dfs1(idx+1 , sub_str)
        #     dfs1(idx+1 , sub_str + text1[idx])

        #     return
        
        # dfs1(0 , "")

        # n2 = len(text2)
        # def dfs2(idx , sub_str):
        #     sub_text2.add(sub_str)
        #     if idx == n2:
        #         return 

        #     # if sub_str in sub_text2:
        #     #     return 
            

        #     dfs2(idx+1 , sub_str)
        #     dfs2(idx+1 , sub_str + text2[idx])

        #     return
        
        # dfs2(0 , "")

        # max_len = 0
        # for sub_str in sub_text1:
        #     if sub_str in sub_text2:
        #         max_len = max(max_len , len(sub_str))

        # return max_len



