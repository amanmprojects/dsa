class Solution:
    def maxSum(self, nums: List[int]) -> int:
        present = set()
        s = 0
        
        for n in nums:
            if n not in present and n > 0:
                present.add(n)
                s += n
        
        if s == 0:
            s = max(nums)

        return s
