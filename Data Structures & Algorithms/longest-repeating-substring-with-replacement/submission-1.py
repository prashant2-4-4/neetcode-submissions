from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        left = 0
        right = 0
        n = len(s)
        max_score = 0
        while(right < n):
            count[s[right]] += 1
            while (right - left + 1 - max(count.values()) > k):
                count[s[left]] -= 1
                left += 1

            max_score = max(max_score , right-left+1)

            right+=1

        return max_score


            

        