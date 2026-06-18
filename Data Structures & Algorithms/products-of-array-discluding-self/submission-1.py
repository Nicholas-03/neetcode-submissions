class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        zero = 0

        for n in nums:
            if n != 0:
                product *= n
            else:
                zero += 1

        if zero > 1:
            return [0] * len(nums)

        if zero == 0:
            for n in nums:
                res.append(int(product / n))
        else:
            for n in nums:
                if n == 0:
                    res.append(product)
                else:
                    res.append(0)

        return res