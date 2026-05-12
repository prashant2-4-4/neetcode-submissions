from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited_set = defaultdict(list)

        for st in strs:
            sorted_st = "".join(sorted(st))
            visited_set[sorted_st].append(st)
        
        result = []
        for value in visited_set.values():
            result.append(value)
        
        return result
        

            
        