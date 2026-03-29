class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = count.get(i,0) + 1
        
        sorted_count = sorted(count.items(),key=lambda x:x[1], reverse=True)

        first_k = sorted_count[:k]
        result = [num for num,freq in first_k]
        return result
        


