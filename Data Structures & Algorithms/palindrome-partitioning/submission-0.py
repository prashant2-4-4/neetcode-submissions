class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def ispalin(i , j):
            while i < j:
                if s[i] != s[j]:
                    return False
                
                i += 1
                j -= 1
            return True

        def recursion(start):
            if start == len(s):
                ans.append(path[:])
                return
            
            for end in range(start , len(s)):
                if ispalin(start , end):
                    path.append(s[start : end+1])
                    recursion(end+1)
                    path.pop()
    
        
        recursion(0)
        return ans