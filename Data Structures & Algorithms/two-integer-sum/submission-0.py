class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        numDict[nums[0]] = 0

        for i in range(1, len(nums)):
            if target - nums[i] in numDict:
                return [numDict[target - nums[i]], i]
            else:
                numDict[nums[i]] = i


        return None