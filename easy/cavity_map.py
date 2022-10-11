def cavityMap(grid):
    # Write your code here
    n = len(grid)
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            current = grid[i][j]
            top = grid[i-1][j]
            left = grid[i][j-1]
            right = grid[i][j+1]
            bottom = grid[i+1][j]
            
            if current > max(top, bottom, left, right):
                grid[i] = ','.join(grid[i]).split(',')
                grid[i][j] = 'X'
                grid[i] = ''.join(grid[i])
    
    return grid