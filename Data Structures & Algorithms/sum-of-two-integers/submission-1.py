class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a ^ b → gives sum without carry
        # (a & b) << 1 → gives carry
        # Repeat until carry becomes 0

        # Your code works perfectly for positive integers, but for negative numbers in Python, it can break or loop forever. That’s because Python integers are not fixed-width (they’re not limited to 32 bits like in C/Java). Internally, Python behaves as if negatives have infinite leading 1s in binary, so the carry may never become zero.

        # for negative lets add mask and mask posive

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while (b):

            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        if a <= max_int:
            return a
        
        else:
            return ~(a^mask)
        