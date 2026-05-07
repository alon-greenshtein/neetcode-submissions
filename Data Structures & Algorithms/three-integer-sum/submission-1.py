class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            start, end = i + 1, n - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s < 0:
                    start += 1
                elif s > 0:
                    end -= 1
                else:
                    res.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1

        return [list(x) for x in res]
        