from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(list)
        n = len(words)

        for i in range(1 , n):
            first_word = words[i-1]
            second_word = words[i]
            # print(first_word , second_word)
            for j in range(min(len(first_word) , len(second_word))):
                if first_word[j] != second_word[j]:
                    graph[first_word[j]].append(second_word[j])
                    break
            
            if first_word.startswith(second_word) and len(first_word) > len(second_word):
                return ""
        
        chars = set()
        for ch in words:
            chars.update(ch)

        visited = {}
        orders = []
        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node] = False # currently visiting 

            for ch in graph[node]:
                if not dfs(ch):
                    return False
            
            visited[node] = True
            orders.append(node)

            return True


        
        for node in chars:
            if node not in visited:
                if not dfs(node):
                    return ""

    
        orders.reverse()
        return "".join(orders)

        