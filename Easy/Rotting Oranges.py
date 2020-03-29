import collections
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        i, j = len(grid), len(grid[0])
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c,col in enumerate(row):
                if col == 2:
                    queue.append((r, c, 0))



        def check(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < i and 0 <= nc < j:
                    yield nr, nc

        mins = 0
        while queue:
            r,c,mins = queue.popleft()

            for m,n in check(r,c):
                if grid[m][n] == 1:
                    grid[m][n] = 2
                    queue.append((m,n,mins+1))

        if 1 in [item for sublist in grid for item in sublist]:
            return -1

        return mins

                
            
        