class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited_dict = Counter(nums)

        max_len = 0

        for key in list(visited_dict.keys()):
            k = key
            count = 0
            while (k in visited_dict) and (k-1 not in visited_dict):
                count += 1
                del visited_dict[k]
                k += 1
  
            max_len = max(max_len , count)
        
        return max_len

        