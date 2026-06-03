class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
        output = []
        def backtrack(i , str_old):
            if i == len(digits):
                output.append(str_old)
                return

            for ch in phone_map[digits[i]]:
                str_old += ch
                backtrack(i+1 , str_old)
                str_old = str_old[:-1]
        
        backtrack(0 , "")
        return output


        