class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        peaks, valleys = 0, 0
        for n in range(num1, num2+1):
            nstr = str(n)
            for i in range(1, len(nstr)-1):
                l, r, curr = int(nstr[i-1]), int(nstr[i+1]), int(nstr[i])
                if l < curr > r:
                    peaks += 1
                elif l > curr < r:
                    valleys += 1
        
        return peaks + valleys
