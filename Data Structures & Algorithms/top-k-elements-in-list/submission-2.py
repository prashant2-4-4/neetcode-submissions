from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #o(n) using bucket sort

        num_list= Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        print(freq)

        for num , fq in num_list.items():
            freq[fq].append(num)
        print(freq)
        res = []

        #now collect result from back

        for i in range(len(freq)-1 , 0 , -1):
            res.extend(freq[i])

            
            if len(res) >= k:
                return res


        
        
        #O(nlogn) in solution
        # num_list = Counter(nums)
        # sorted_lst = sorted(num_list.items() , key = lambda x : x[1] , reverse = True)
        # return list(x[0] for x in sorted_lst[:k])

        