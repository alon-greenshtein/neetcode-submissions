class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        for i in range(len(nums)):
            p = 0
            for j in range(i, len(nums)):
                p += nums[j]
                s = max(s, p)
        return s


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)

        return best        