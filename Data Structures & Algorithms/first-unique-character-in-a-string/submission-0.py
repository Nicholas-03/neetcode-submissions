class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}

        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = 0
            map[s[i]] += 1

        for key, value in map.items():
            if value == 1:
                return s.index(key)

        return -1