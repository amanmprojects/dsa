from math import ceil
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1 + nums2)
        total = len(combined)

        if total % 2 == 0:
            return (combined[total // 2 - 1] + combined[total // 2]) / 2
        
        return combined[total // 2]