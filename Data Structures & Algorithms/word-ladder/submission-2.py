from collections import defaultdict , deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def isdiffernce(curr_word , next_word):
            if len(curr_word) != len(next_word):
                return float('inf')
            
            count = 0
            for i , j in zip(curr_word , next_word):
                if i!=j:
                    count += 1

            return count
        
        adj_list = defaultdict(list)
        wordList = [beginWord] + wordList
        n = len(wordList)
        for i in range(n):
            curr_word = wordList[i]
            for j in range(i+1 , n):
                next_word = wordList[j]
                if isdiffernce(curr_word , next_word) == 1:
                    adj_list[curr_word].append(next_word)
                    adj_list[next_word].append(curr_word)
        
        # print(adj_list)

            

        
        visited = set()
        # visited.add(beginWord)
        queue = deque()
        queue.append((beginWord,1))
        visited.add(beginWord)
        while queue:
            # print(queue)
            word , count = queue.popleft()
            if word == endWord:
                return count
        
            
            
            for new_word in adj_list[word]:
                if new_word not in visited:
                    queue.append((new_word , count+1))
                    visited.add(new_word)
        
        return 0


        