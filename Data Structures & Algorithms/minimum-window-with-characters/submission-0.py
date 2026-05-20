from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        
        countT , window = {} , {}

        for c in t:
            countT[c] = 1+countT.get(c , 0)
        
        have , need = 0 , len(countT)

        l = 0
        res , reslen = [-1 , -1] , float('inf')
        for r in range(len(s)):
            # checking the value and if that value is equal to count of t append have
            c = s[r]
            window[c] = 1 + window.get(c , 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have==need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                
                #pop from left of our window to shrink the array
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1

        l , r = res
        return "" if reslen==float('inf') else s[l:r+1]

            
