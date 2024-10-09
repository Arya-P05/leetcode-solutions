class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashm = defaultdict(int)
        count = 0

        for row in grid:
            hashm[str(row)] += 1
        
        for idx in range(len(grid[0])):
            col = []

            for jdx in range(len(grid)):
                col.append(grid[jdx][idx])

            count += hashm[str(col)]

        return count