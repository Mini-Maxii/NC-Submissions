class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1;
        for i in range(len(nums)):
            res[i] = prefix #assigns res[i] to previous element because we're trying to get index before
            prefix *= nums[i] #updates prefix by multiplying in the current element, so that on the next loop it represents the product 
            #of everything to the left of the next index.
        postfix = 1
        for i in range(len(nums) -1,-1,-1):
            res[i] *= postfix #start at the end and multiple the previous element by res[i]
            postfix *= nums[i] #update postfix 
        return res
            