class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = []
        n = len(s)
        output = s[0]
        max_len = 1

        for i in range(n):
            for j in range(i+1 , n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if max_len < (j-i+1):
                        output = s[i:j+1]
                        max_len = (j-i+1)
                    # output.append((s[i:j+1] , j-i+1))
        # output.sort(key= lambda x : x[1])
        # return output[-1][0]
        return output