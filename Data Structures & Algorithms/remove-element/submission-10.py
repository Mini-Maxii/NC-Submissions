class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #go through list and remove val in place
        #that means we have to shift over elements
        #so, two pointers, index and a slider
        #the index checks position, the slider checks the next
        #if they are the same the index is not val, proceed

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i