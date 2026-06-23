class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        res = nums[0]
        for i in range(len(nums)):
            p = 0
            for j in range(i, len(nums)):
                p += nums[j]
                s = max(s, p)
            res = max(res, s)
        return res


        