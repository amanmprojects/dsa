class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        if len(nums) == 1: return nums[0]
        elif len(nums) == 2: return min(nums[0], nums[1])

        while l < r:
            mid = int((l+r)/2)
            print(f"l = {l}, r = {r}, mid = {mid}")
            if(nums[mid] > nums[r]): l = mid+1
            else: r = mid

        return nums[l]




