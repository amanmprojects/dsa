from typing import List

# Brute Force Solution
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area  = 0
        for i, h in enumerate(heights):
            l = r = i
            while(l>=0 and heights[l] >= h): l -= 1
            l += 1
            while(r<len(heights) and heights[r] >= h): r += 1

            max_area = max(max_area, h*(r-l))
        
        return max_area


