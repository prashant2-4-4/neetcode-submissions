class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = []

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                good.append(triplet)
        

        ans = [False] * 3
        for triplet in good:
            if triplet[0] == target[0]:
                ans[0] = True
            
            if triplet[1] == target[1]:
                ans[1] = True
            
            if triplet[2] == target[2]:
                ans[2] = True
        
        return all(ans)
        