class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        ans = {}

        for n in nums:
            if n not in map:
                map[n] = 0
            map[n] += 1

            if map[n] not in ans:
                ans[map[n]] = set()
            ans[map[n]].add(n)
            if (map[n] - 1 > 0):
                ans[map[n] - 1].remove(n)

        answer = []
        i = 0
        while len(answer) < k:
            answer.extend(list(ans[len(ans) - i]))
            i += 1

        return answer[:k]

