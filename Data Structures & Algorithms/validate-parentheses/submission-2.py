class Solution:
    def isValid(self, s: str) -> bool:
        match = {')' : '(' 
        , '}' : '{' 
        , ']' : '[' }
        stack = []
        for st in s:
            if st in match.values():
                stack.append(st)
            
            else:
                if not stack:
                    return False
                if stack[-1] == match[st]:
                    stack.pop()
                else:
                    return False
        
        return len(stack)==0
        