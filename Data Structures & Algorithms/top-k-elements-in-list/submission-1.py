from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_list = Counter(nums)
        sorted_lst = sorted(num_list.items() , key = lambda x : x[1] , reverse = True)
        return list(x[0] for x in sorted_lst[:k])

        