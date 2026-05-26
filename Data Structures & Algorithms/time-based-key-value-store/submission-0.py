from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timestamp_store = defaultdict()
        self.name_timestamp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_store[(key , timestamp)] = value
        self.name_timestamp[key].append(timestamp)
        return None
        

    def get(self, key: str, timestamp: int) -> str:
        lst = list(self.name_timestamp[key])
        print(lst)
        l, r = 0 , len(lst)-1
        result = ""
        
        while(l<=r):
            mid = (l+r)//2
            if lst[mid] <= timestamp:
                result =  self.timestamp_store[key , lst[mid]]
                l = mid + 1
            else:
                r = mid - 1
        
        return result



        
