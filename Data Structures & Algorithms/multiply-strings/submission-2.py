class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == '0' or num2 == '0':
            return '0'
        # max length can m + n
        m = len(num1)
        n = len(num2)
        #grade school multiplications
        result = [0] * (m+n)

        for i in range(m-1 , -1 , -1):
            for j in range(n-1 , -1 , -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                p1 , p2 = i+j , i+j + 1 # p1 is remaninder and p2 is for main value and very we filling from back

                out = mul + result[p2] # mul + result[p2] whatever value was there

                result[p2] = out%10 # remainder
                result[p1] += out//10 # carry main value and adding whaterver there was intially

        
        return "".join(str(d) for d in result).lstrip('0') # removing leaeding zero