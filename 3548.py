#3548. Equal Sum Grid Partition II

class Solution:
    def canPartitionGrid(self, grid):
        from collections import Counter
        
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        
        # ---------- Horizontal ----------
        top = Counter()
        bottom = Counter()
        
        for row in grid:
            for v in row:
                bottom[v] += 1
        
        sum_top = 0
        
        for i in range(m - 1):
            for v in grid[i]:
                top[v] += 1
                bottom[v] -= 1
                if bottom[v] == 0:
                    del bottom[v]
                sum_top += v
            
            sum_bottom = total - sum_top
            
            if sum_top == sum_bottom:
                return True
            
            diff = abs(sum_top - sum_bottom)
            
            # check remove from top
            if sum_top > sum_bottom:
                rows, cols = i + 1, n
                
                if diff in top:
                    if rows > 1 and cols > 1:
                        return True
                    if rows == 1:
                        if grid[0][0] == diff or grid[0][-1] == diff:
                            return True
                    if cols == 1:
                        if grid[0][0] == diff or grid[i][0] == diff:
                            return True
            
            else:
                rows, cols = m - i - 1, n
                
                if diff in bottom:
                    if rows > 1 and cols > 1:
                        return True
                    if rows == 1:
                        r = i + 1
                        if grid[r][0] == diff or grid[r][-1] == diff:
                            return True
                    if cols == 1:
                        if grid[i+1][0] == diff or grid[m-1][0] == diff:
                            return True
        
        # ---------- Vertical ----------
        left = Counter()
        right = Counter()
        
        for j in range(n):
            for i in range(m):
                right[grid[i][j]] += 1
        
        sum_left = 0
        
        for j in range(n - 1):
            for i in range(m):
                v = grid[i][j]
                left[v] += 1
                right[v] -= 1
                if right[v] == 0:
                    del right[v]
                sum_left += v
            
            sum_right = total - sum_left
            
            if sum_left == sum_right:
                return True
            
            diff = abs(sum_left - sum_right)
            
            if sum_left > sum_right:
                rows, cols = m, j + 1
                
                if diff in left:
                    if rows > 1 and cols > 1:
                        return True
                    if cols == 1:
                        if grid[0][0] == diff or grid[-1][0] == diff:
                            return True
                    if rows == 1:
                        if grid[0][0] == diff or grid[0][j] == diff:
                            return True
            
            else:
                rows, cols = m, n - j - 1
                
                if diff in right:
                    if rows > 1 and cols > 1:
                        return True
                    if cols == 1:
                        c = j + 1
                        if grid[0][c] == diff or grid[-1][c] == diff:
                            return True
                    if rows == 1:
                        if grid[0][j+1] == diff or grid[0][-1] == diff:
                            return True
        
        return False