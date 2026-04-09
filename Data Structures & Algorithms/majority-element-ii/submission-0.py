class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1

        res = []
        
        for n in freq.keys():
            if freq[n] > len(nums) // 3:
                res.append(n)
            
        return res