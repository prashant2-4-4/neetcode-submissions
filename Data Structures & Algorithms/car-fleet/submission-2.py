class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # cars = []

        # for i , j in zip(position , speed):
        #     cars.append((i , j))
        cars = list(zip(position , speed))
        # cars.sort(key = lambda x : x[0])
        cars.sort(reverse = True)

        stack = []
        # print(cars)
        for pos , speed in cars:
            time = (target - pos)/speed
            stack.append(time)
            # print(stack , time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        