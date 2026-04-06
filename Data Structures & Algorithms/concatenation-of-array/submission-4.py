class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0]* 2 * len(nums)

        for i in range(len(nums)):
            res[i], res[len(nums)+i] = nums[i], nums[i]
        
        return res