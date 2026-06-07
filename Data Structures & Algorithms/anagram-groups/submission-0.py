class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i in range(len(strs)):
            s = strs[i]
            s = list(s)
            s.sort()
            s = "".join(s)

            if (s in seen):
                seen[s].append(strs[i])
            else:
                seen[s] = [strs[i]]

        return list(seen.values())