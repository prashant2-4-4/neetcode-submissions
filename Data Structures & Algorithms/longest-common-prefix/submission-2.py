class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        n = len(strs)
        for i in range(1 , n):
            st = strs[i]
            min_len = min(len(common_prefix) , len(st))
            for j in range(min_len):
                if common_prefix[j] != st[j]:
                    common_prefix = common_prefix[:j]
                    break
            

            common_prefix = common_prefix[:min_len]

        return common_prefix