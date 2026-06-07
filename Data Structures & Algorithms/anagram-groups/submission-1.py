class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for s in strs:
            sorted_key = "".join(sorted(s))

            if sorted_key not in hashMap:
                hashMap[sorted_key] = []

            hashMap[sorted_key].append(s)

        return list(hashMap.values())