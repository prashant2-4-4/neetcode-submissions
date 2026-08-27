from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        size = [1]*n

        def find(x):
            if parent[x] == x:
                return parent[x]
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)
            if p1 == p2:
                return

            if size[p1] > size[p2]:
                size[p1] += size[p2]
                parent[p2] = p1
            
            else:
                parent[p1] = p2
                size[p2] += size[p1]

        email_to_account = {}
        for i , account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(i , email_to_account[email])
                else:
                    email_to_account[email] = i

        print(email_to_account)
        print(parent)
        group = defaultdict(list)

        for email , account_index in email_to_account.items():
            root = find(account_index)
            group[root].append(email)
        
        print(group)
        result = []
        # group.sort(lambda x : len(x.values()))
        group = dict(sorted(group.items() ,key = lambda x : len(x[1])))
        for root , email in group.items():
            email.sort()
            name = accounts[root][0]
            result.append([name] + email)
        
        return result
        

