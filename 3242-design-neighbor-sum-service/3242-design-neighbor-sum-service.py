class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.grid = grid
        self.indices = {}
        for r in range(self.n):
            for c in range(self.n):
                self.indices[grid[r][c]] = (r, c)

        self.adjDirections = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.diagDirections = [(1, 1), (1, -1), (-1, 1), (-1, -1)]      

    def adjacentSum(self, value: int) -> int:
        r, c = self.indices[value]
        sum = 0

        for dr, dc in self.adjDirections:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                sum += self.grid[nr][nc]

        return sum

    def diagonalSum(self, value: int) -> int:
        r, c = self.indices[value]
        sum = 0

        for dr, dc in self.diagDirections:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                sum += self.grid[nr][nc]

        return sum
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)