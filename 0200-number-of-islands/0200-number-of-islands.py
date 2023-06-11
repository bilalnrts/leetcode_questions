class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowCount = len(grid)
        columnCount = len(grid[0])
        visited = set()
        islandCount = 0
        
        def bfs(row, column):
            directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
            myQueue = []
            myQueue.append([row,column])
            visited.add((row, column))
            
            while (myQueue):
                row, column = myQueue.pop(0)
                
                for rowDirection, columnDirection in directions:
                    newRow = rowDirection + row
                    newColumn = columnDirection + column
                    
                    if ((newRow, newColumn) not in visited and
                        newRow in range(rowCount) and
                        newColumn in range(columnCount) and
                        grid[newRow][newColumn] == "1"):
                        myQueue.append([newRow, newColumn])
                        visited.add((newRow, newColumn))
        
        for row in range(rowCount):
            for column in range(columnCount):
                if ((row, column) not in visited and
                   grid[row][column] == "1"):
                    islandCount += 1
                    bfs(row, column)
        
        return (islandCount)