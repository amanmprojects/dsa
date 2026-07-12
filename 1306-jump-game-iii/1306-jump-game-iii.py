class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        size = len(arr)

        def dfs(i):
            if i not in range(0, size) or arr[i] < 0:
                return False
            
            elif arr[i] == 0:
                return True
            
            else:
                arr[i] *= -1
                return dfs(i + arr[i]) or dfs(i - arr[i])
        
        return dfs(start)
