class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        for i in range(n):
            while(stack and temperatures[i] > temperatures[stack[-1]]):
                result[stack[-1]] = i-stack[-1]
                stack.pop()
                
            
            stack.append(i)
        
        return result



            # print(stack , temperatures[i]) 
            # if temperatures[i] > stack[-1][0]:
            #     result.append(stack[-1][1]+1)
            #     stack.pop()
            #     stack.append([temperatures[i] , 0])
            # else:
            #     stack.append([temperatures[i] , 0])
            
            # for i in range(len(stack)):
            #         stack[i][1] += 1

            # print(stack)
        result.append(stack[-1][1])
        return result
