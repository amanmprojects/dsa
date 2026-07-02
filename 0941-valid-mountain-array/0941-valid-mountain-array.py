class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        differences = []
        for i in range(1, len(arr)):
            differences.append(arr[i] - arr[i-1])
            if differences[-1] == 0:
                return False
        
        if differences[0] < 0:
            return False

        if differences[-1] > 0:
            return False

        decreasing = False

        for diff in differences:
            if not decreasing:
                if diff < 0:
                    decreasing = True
                    continue

            if decreasing:
                if diff > 0:
                    return False

        return True 


