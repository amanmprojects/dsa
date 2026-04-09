class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums

        nums1 = -1
        nums2 = -1
        cnt1 = cnt2 = 0

        for i in range(0, len(nums)):
            if nums[i] == nums1:
                cnt1 += 1
            elif nums[i] == nums2:
                cnt2 += 1
            elif cnt1 == 0:
                nums1 = nums[i]
                cnt1 = 1
            elif cnt2 == 0:
                nums2 = nums[i]
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            
        cnt1 = cnt2 = 0

        for n in nums:
            if n == nums1:
                cnt1 += 1
            elif n == nums2:
                cnt2 += 1
    
        res = []
        if cnt1 > len(nums) // 3:
            res.append(nums1)
        if cnt2 > len(nums) // 3:
            res.append(nums2)

        return res
            

            