from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        res = []
        p = len(digits)-1
        carry = 0
        while p >= 0:
            res.insert(0,(digits[p]+carry)%10)
            carry = (digits[p]+carry) // 10
            p -= 1
        if carry:
            res.insert(0, carry)

        return res