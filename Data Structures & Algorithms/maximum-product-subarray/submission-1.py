class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        maxProd = nums[0]

        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                maxProd = max(prod, maxProd)

        return maxProd