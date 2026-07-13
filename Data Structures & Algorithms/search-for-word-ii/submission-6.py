# from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #built Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children: # if ch is not in children create it
                    node.children[ch] = TrieNode()
                
                node = node.children[ch] # getting new node for ch
            node.word = word
        
        row, col = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = []

        def dfs(r,c,node):
            ch = board[r][c]

            if ch not in node.children:
                return 
            
            node = node.children[ch]
            if node.word:
                ans.append(node.word)
                node.word = None #avoid duplication

            board[r][c] = '#' # marking visited for current running

            for dx , dy in directions:
                if 0 <= dx+r < row and 0 <= dy+c < col:
                    dfs(r+dx , c+dy , node)

            board[r][c] = ch 


        for r in range(row):
            for c in range(col):
                dfs(r, c, root)

        return ans




        # row , col = len(board) , len(board[0])
        # directions = [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]
        # ans = []

        # def valid(i , j):
        #     if 0 <= i < row and 0 <= j < col:
        #         return True
            
        #     return False

        # def dfs(r,c , idx , visited):
        #     if idx == n:
        #         return True
            
        #     if not valid(r,c) or board[r][c] != word[idx] or (r,c) in visited:
        #         return False

        #     visited.add((r,c))

        #     for dx , dy in directions:
        #         if dfs(r+dx , c + dy , idx+1 , visited):
        #             return True
            
        #     visited.remove((r,c))
        #     return False


        # for word in words:
        #     found = False
        #     for r in range(row):
        #         for c in range(col):
        #             n = len(word)
        #             if board[r][c] == word[0]:
        #                 if dfs(r , c , 0 , set()):
        #                     ans.append(word)
        #                     found = True
        #                     break
        #         if found:
        #             break
        #         #     queue = deque()
        #         #     visited = set()
        #         #     n = len(word)
        #         #     if board[r][c] == word[0]:
        #         #         queue.append((r, c , 1))
        #         #         visited.add((r,c))
        #         #         while queue:
        #         #             rpx , cpy , idx = queue.popleft()
        #         #             if idx == n:
        #         #                 ans.append(word)
        #         #                 flag = True
        #         #                 break
        #         #             for dx , dy in directions:
        #         #                 rx = rpx + dx
        #         #                 cy = cpy + dy
        #         #                 if valid(rx , cy) and idx < n and word[idx] == board[rx][cy] and ((rx , cy) not in visited):
        #         #                     queue.append((rx , cy , idx+1))
        #         #                     visited.add((rx , cy))
        #         #     if flag:
        #         #         break
                
        #         # if flag:
        #         #     break
            
        
        # return ans









        