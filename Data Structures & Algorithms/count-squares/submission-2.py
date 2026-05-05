class CountSquares:

    def __init__(self):
        self.tbl = {}
        

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.tbl[point] = self.tbl.get(point , 0) + 1
        return None

    def count(self, point: List[int]) -> int:
        point = tuple(point)
        x , y = point
        total = 0
        for px , py in list(self.tbl.keys()): # later if mutated we do get effected
            if x == px or y == py: # same exact point
                continue

            # if abs(x-px) == abs(y-py): # only rectange removing square
            #     continue

            if abs(x - px) != abs(y-py): # check rectange criteria
                continue

            
            
            count_x = self.tbl.get((px , y) , 0)
            count_y  = self.tbl.get((x , py) , 0)

            total += self.tbl[(px , py)] * count_x * count_y
        
        return total
            

                                
                


        
