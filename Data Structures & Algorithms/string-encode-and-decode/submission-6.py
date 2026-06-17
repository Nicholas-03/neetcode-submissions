class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + '#' + s

        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        
        i = 0
        while(i < len(s)):
            k = 1
            while s[i + k] != '#':
                k += 1
            print(s[i:i+k])
            length = int(s[i:i + k])
            ans.append(s[i + k + 1 : i + k + length + 1])
            i += length + k + 1

        return ans
