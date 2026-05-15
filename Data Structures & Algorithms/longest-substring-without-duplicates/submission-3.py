class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # it will be done using sliding window

        visited_set = set()
        left = 0
        res= 0

        for right in range(len(s)):
            while s[right] in visited_set:
                visited_set.remove(s[left])
                left += 1

            visited_set.add(s[right])
            res = max(res , right-left+1)
        
        return res
            


        
        
        # visited_set = set()
        # res = 0
        # for st in s:
        #     if st in visited_set:
        #         res = max(res , len(visited_set))
        #         visited_set = set()
        #     visited_set.add(st)
            
        
        # res = max(res , len(visited_set))
        # return res

        