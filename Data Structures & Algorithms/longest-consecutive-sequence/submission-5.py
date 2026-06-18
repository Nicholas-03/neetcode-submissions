class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        maxSeq = 0
        seq = 1

        # if len(nums) == 1:
        #     return 1

        for i in range(len(nums)):
            if i < len(nums) - 1:
                if nums[i + 1] - nums[i] == 1:
                    seq += 1
                elif nums[i + 1] - nums[i] > 1:
                    maxSeq = max(seq, maxSeq)
                    seq = 1

            else:
                maxSeq = max(seq, maxSeq)

        return maxSeq