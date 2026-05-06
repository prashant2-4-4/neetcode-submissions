class Solution:
    def longestPalindrome(self, s: str) -> str:
        # output = []
        # n = len(s)
        # output = s[0]
        # max_len = 1

        # for i in range(n):
        #     for j in range(i+1 , n):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             if max_len < (j-i+1):
        #                 output = s[i:j+1]
        #                 max_len = (j-i+1)
        #             # output.append((s[i:j+1] , j-i+1))
        # # output.sort(key= lambda x : x[1])
        # # return output[-1][0]
        # return output
        output = ""
        max_len = 0
        n = len(s)
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # when loop ends, s[left+1:right] is the palindrome
            return s[left+1:right]

        for i in range(n):
            odd  = expand(i, i)    # odd length
            even = expand(i, i+1)
            if len(odd) > max_len:
                output = odd
                max_len = len(odd)

            if len(even) > max_len:
                output = even
                max_len = len(even)
        
        return output

