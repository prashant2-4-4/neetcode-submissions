class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        end = len(digits)-1

        flag = False
        while end >= 0:
            if digits[end] == 9:
                digits[end] = 0
            else:
                digits[end] += 1
                flag = True
                break
            
            end -= 1
        
        if flag:
            return digits
        else:
            return ['1'] + digits

        