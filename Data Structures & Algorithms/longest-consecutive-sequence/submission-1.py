class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))

        current_streak = 1
        longest_streak = 1

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i + 1] == sorted_nums[i] + 1:
                current_streak += 1
            else:
                current_streak = 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

            



        
        
        
