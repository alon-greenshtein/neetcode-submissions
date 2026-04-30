class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Output = []

        product = 1
        for x in nums:
            Output.append(product)
            product *= x
    
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            Output[i] *= product    
            product *= nums[i]
        
        return Output
            
        
        