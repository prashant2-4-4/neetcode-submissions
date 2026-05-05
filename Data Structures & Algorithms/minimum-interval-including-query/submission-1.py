import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # time complexity o(mlogm)(sorting) + o(nlogn)(sorting) + o(nlogm)(last loop running)
        # space complexity o(n+m)

        output = []
        heap = []

        for i in range(len(queries)):
            queries[i] = (queries[i] , i)
        
        # print(queries)
        queries.sort(key = lambda x : x[0])

        intervals.sort(key = lambda x : x[0])

        # print(queries , intervals)

        for query, original_index in queries:
            i = 0
            while i < len(intervals) and intervals[i][0] <= query:
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap , (size , intervals[i][1]))
                i += 1

            while heap and query > heap[0][1]:
                heapq.heappop(heap) 
            # if heap:
            #     output.append((heap[0][0] , original_index))
            
            # else:
            #     output.append((-1 , original_index))
            
            # output.append((heap[0][0] , original_index) if heap else (-1 , original_index))
            output.append((heap[0][0] if heap else -1 , original_index))

        output.sort(key = lambda x : x[1])
        res = [out for out , _ in output]
        return res

        