class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = [False] * (total+1)
        dp[0] = True
        # print(total)
        for s in stones:
            for i in range(total , s-1 , -1):
                # print(i , i-s)
                dp[i] = dp[i] or dp[i-s]

        # print(dp)
        half_lower = total//2
        while half_lower >= 0:
            if dp[half_lower] == True:
                return total - 2*half_lower

            half_lower -= 1
        

        return -1

        