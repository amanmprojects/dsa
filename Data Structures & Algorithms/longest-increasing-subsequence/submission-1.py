class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        LIS = {}

        maxDepth = 0

        def getMaxDepth(i) -> int: 
            if i in LIS: return LIS[i]
            curr = nums[i]
            md = 1
            for j in range(i+1, len(nums)):
                if nums[j] > curr:
                    res = getMaxDepth(j)
                    md = max(md, res+1)
            LIS[i] = md
            return md
        
        for i in range(len(nums)):
            m = getMaxDepth(i)
            maxDepth = max(maxDepth, m)

        return maxDepth
