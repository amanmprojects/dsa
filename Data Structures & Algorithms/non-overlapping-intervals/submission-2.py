class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ic = intervals.copy()
        ic.sort()
        count = 0
        i = 0
        while True:
            print(i, ic)
            if i == len(ic)-1:
                break 
    
            # Overlap with the next interval, remove the next interval
            if ic[i][1] > ic[i+1][0]:
                if ic[i][1]>ic[i+1][1]:
                    ic.pop(i)
                    count += 1
                else:
                    ic.pop(i+1)
                    count += 1
            else:
                i+=1
        
        return count
        

            

        