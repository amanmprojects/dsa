class Solution:
    def mirrorDistance(self, n: int) -> int:
        mirror = int(''.join(reversed(str(n))))
        return abs(n - mirror)