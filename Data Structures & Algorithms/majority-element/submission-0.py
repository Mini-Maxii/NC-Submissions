class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_count = {}

        for n in nums:
            my_count[n] = my_count.get(n,0) + 1
        
        return max(my_count, key=my_count.get)