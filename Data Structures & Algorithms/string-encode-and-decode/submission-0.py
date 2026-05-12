class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        res = []
        while(i < len(s)):
            j = i

            while s[j] != '#':
                j += 1
            # print(i , j)
            length = int(s[i : j])
            word = s[j+1 : j+length+1]
            res.append(word)
            i = j+length+1
        return res

            


