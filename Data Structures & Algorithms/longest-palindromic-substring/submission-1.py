class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = []
        n = len(s)

        for i in range(n):
            output.append((s[i] , 1))
            for j in range(i+1 , n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    output.append((s[i:j+1] , j-i+1))
        output.sort(key= lambda x : x[1])
        return output[-1][0]