class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0, 0, 0]

        for n in nums:
            freq[n] += 1

        k = 0
        
        for i in range(3):
            for j in range(k, k + freq[i]):
                nums[j] = i
            k += freq[i]

        return
        


# def sortArray(self, nums: List[int]) -> List[int]:
    
#     def mergeSort(split: List[int]) -> List[int]:
#         if len(split) < 2:
#             return split
        
#         mid = len(split) // 2

#         left = mergeSort(split[:mid])
#         right = mergeSort(split[mid:])

#         l, r = 0, 0

#         while l < len(left) or r < len(right):
#             if l == len(left):
#                 split[l + r] = right[r]
#                 r += 1
#             elif r == len(right):
#                 split[l + r] = left[l]
#                 l += 1
#             elif left[l] >= right[r]:
#                 split[l + r] = right[r]
#                 r += 1
#             else:
#                 split[l + r] = left[l]
#                 l += 1 

#         return split

#     return mergeSort(nums)




