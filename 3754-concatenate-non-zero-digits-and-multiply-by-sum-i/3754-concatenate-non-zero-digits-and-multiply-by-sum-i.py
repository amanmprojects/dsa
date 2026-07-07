class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        s = 0
        while n != 0:
            units = n%10
            if units != 0:
                x = x*10
                x += (units)
                s += (units)
            n = n // 10
        
        xf = 0
        while x != 0:
            xf *= 10
            xf += x%10
            x //= 10
        
        return xf * s
        
