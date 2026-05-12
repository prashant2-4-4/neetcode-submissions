class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        visited_set = {}
        for num in nums:
            if num in visited_set:
                return True
            visited_set[num] = 1
        return False
        