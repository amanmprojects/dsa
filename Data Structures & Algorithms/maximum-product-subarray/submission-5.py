class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = currMax = maxProd = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], currMax * nums[i], currMin * nums[i])

            currMin = min(nums[i], currMax * nums[i], currMin * nums[i])

            currMax = temp

            maxProd = max(maxProd, currMax)
        
        return maxProd