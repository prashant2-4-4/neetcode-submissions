from collections import defaultdict
class Solution:

    # def dfs(self , to , temp):
    #     if len(temp) == self.len_trip:
    #         self.res.append(temp)
    #         return 
        

    #     for des in list(self.visted_from[to]):
    #         self.visted_from[to].remove(des)
    #         # print(to , des)
    #         # print(self.visted_from)
    #         self.dfs(des , temp + [des])
    #         self.visted_from[to].append(des) # for other branches
        

        

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # self.visted_from = defaultdict(list)
        # self.res = []
        # self.len_trip = 1
        # for fro , to in tickets:
        #     self.len_trip += 1
        #     self.visted_from[fro].append(to)
        
        # # print(self.visted_from)
        # self.dfs('JFK' , ['JFK'])
        # # print(self.res)
        # self.res.sort()
        # return self.res[0]

        visited = defaultdict(list)
        res = []
        len_trip = len(tickets) + 1
        for fro , to in sorted(tickets , reverse = True):
            visited[fro].append(to)

        def dfs(airport):
            while visited[airport]:
                next_des = visited[airport].pop() #last value or lexi smallest
                dfs(next_des) 
            res.append(airport) # add back only when no more destination

        dfs("JFK")
        return res[::-1] # reversed stored
