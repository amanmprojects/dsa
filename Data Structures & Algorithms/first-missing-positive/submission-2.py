class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        i = 0
        hashset = set()

        while i < len(nums):
            hashset.add(nums[i])
            if nums[i] == smallest:
                smallest += 1
                while smallest in hashset:
                    smallest += 1
            i += 1
        
        return smallest