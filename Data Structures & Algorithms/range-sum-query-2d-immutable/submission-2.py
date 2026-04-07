# 1-D prefix sum

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # self.matrix = matrix
        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]        
        for r in range(len(matrix)):
            s = 0
            for c in range(len(matrix[0])):
                s += matrix[r][c]
                self.prefix[r][c] = s
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for r in range(row1, row2+1):
            right = self.prefix[r][col2]
            left = 0 if col1 == 0 else self.prefix[r][col1-1]
            s += (right-left)
        
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)