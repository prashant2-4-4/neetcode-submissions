from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        visited = set()
        deadends = set(deadends)

        queue = deque()
        if "0000" not in deadends:
            queue.append((('0','0','0','0') , 0))
            visited.add(('0','0','0','0'))
        # print(deadends)
        while queue:
            
            state , cnt = queue.popleft()
            if "".join(state) == target:
                return cnt
            
            for i in range(4):
                new_state = state[:i] +tuple(str(int(state[i])+1)[-1]) +  state[i+1:]
                if new_state not in visited and "".join(new_state) not in deadends:
                    queue.append((new_state, cnt+1))
                    visited.add(new_state)
            
            for i in range(4):
                new_val = int(state[i])-1
                if new_val==-1:
                    new_val = 9
                new_state = state[:i] + tuple(str(new_val)) + state[i+1:]
                if new_state not in visited and "".join(new_state) not in deadends:
                    queue.append((new_state, cnt+1))
                    visited.add(new_state)

        return -1

        