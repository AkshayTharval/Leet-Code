class Solution:
    def prisonAfterNDays(self, cells, N):
        while N>0:
            cells2 = []
            cells2.append(0)
            for i in range(1, 7):
                val = 1 if cells[i-1]==cells[i+1] else 0
                cells2.append(val);
            cells2.append(0)
            cells = cells2
            N = (N - 1)%14 # needed or else timeout
            # N = N - 1 # brute force
        return cells;
        