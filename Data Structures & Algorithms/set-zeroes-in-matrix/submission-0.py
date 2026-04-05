class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        # This array holds whether this row should be zeroes
        rowz, colz = [1]*ROWS, [1]*COLS
        
        # Deciding which rows and which cols get to be zeroes
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowz[r] = 0
                    colz[c] = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] *= rowz[r] * colz[c]
        

        


        
            
        
                
        