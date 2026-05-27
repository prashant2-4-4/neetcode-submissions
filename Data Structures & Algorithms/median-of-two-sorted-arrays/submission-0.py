class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #divide and conquer and binary search
        A, B = nums1 , nums2
        # check so that y does not go out of bound
        if len(A) > len(B):
            A , B = B , A

        m , n = len(A) , len(B)

        l , r = 0 , m
        half = (m+n)//2

        while(l<=r):
            x = (l+r)//2
            y = half-x

            Aleft = A[x-1] if x>0 else float('-inf')
            Aright = A[x] if x < m else float('inf')
            Bleft = B[y-1] if y>0 else float('-inf')
            Bright = B[y] if y < n else float('inf')


            if Aleft <= Bright and Bleft <= Aright:
                if (m+n)%2==1:
                    return min(Aright , Bright)
                
                return (min(Aright , Bright) + max(Aleft , Bleft))/2
        
            if Aleft > Bright:
                r = x-1

            else:
                l = x+1