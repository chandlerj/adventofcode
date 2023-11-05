import data


testGrid ="""30373
25512
65332
33549
35390"""

def checkSurroundingTrees(grid, currTree, i, j, gridHeight, gridWidth):
    #print(j, i)
            #rule out boarder trees
    if i == 0 or j == 0 or i == gridHeight -1 or j == gridWidth - 1:
        return True
    # search up
    for h in range(i - 1, -1, -1):
        nextTree = int(grid[h][j])
        if nextTree < int(currTree): 
            if h == 0:
                print(f"UP: marked visible {j},{i}: value - {currTree}")
                return True
        else:
            break
    # search down
    for h in range(i + 1, gridHeight):
        nextTree = int(grid[h][j])
        
        if nextTree < int(currTree): 
            if h == gridHeight - 1:
                print(f"DOWN: marked visible {j},{i}: value - {currTree}")
                return True
            else:
                continue
        else:
            break
    # search left
    for h in range(j - 1, -1, -1):
        nextTree = int(grid[i][h])
        
        if nextTree < int(currTree): 
            if h == 0:
                print(f"LEFT: marked visible {j},{i}: value - {currTree}")
                return True
            else:
                continue
        else:
            break

    # search right
    for h in range(j + 1, gridWidth):
        nextTree = int(grid[i][h])
        
        if nextTree < int(currTree): 
            if h == gridHeight - 1:
                print(f"RIGHT: marked visible {j},{i}: value - {currTree}")
                return True
            else:
                continue
        else:
            break


    return False

def checkTreeViewDist(grid, currTree, i, j, gridHeight, gridWidth):
    visibility = {"up":0, "down":0, "left":0, "right":0}

    #rule out boarder trees
    if i == 0 or j == 0 or i == gridHeight -1 or j == gridWidth - 1:
        return 0 


    # search up
    for h in range(i - 1, -1, -1):
        nextTree = int(grid[h][j])
        if nextTree < int(currTree): 
            visibility["up"] += 1    
        else:
            visibility["up"] += 1
            break
    
    # search down
    for h in range(i + 1, gridHeight):
        nextTree = int(grid[h][j])
        if nextTree < int(currTree): 
            visibility["down"] += 1    
        else:
            visibility["down"] += 1
            break

    # search left
    for h in range(j - 1, -1, -1):
        nextTree = int(grid[i][h])
        if nextTree < int(currTree): 
            visibility["left"] += 1    
        else:
            visibility["left"] += 1
            break
 
    # search right
    for h in range(j + 1, gridWidth):
        nextTree = int(grid[i][h])
        if nextTree < int(currTree): 
            visibility["right"] += 1    
        else:
            visibility["right"] += 1
            break

            
    finalVisibilityScore = 1
    for direction in visibility.values():
        finalVisibilityScore *= direction
    
    return finalVisibilityScore

    
def findVisibleTrees(grid: str) -> int:
    visibleTrees = 0
    grid = grid.split('\n')
    gridHeight = len(grid)
    gridWidth = len(grid[0])
    for i, row in enumerate(grid): # for every row of the grid
        for j, currTree in enumerate(row): # for every element of every row
            if checkSurroundingTrees(grid, currTree, i, j, gridHeight, gridWidth):
                visibleTrees += 1

    return visibleTrees

def findGreatestVisibility(grid):
    highestTreeVisibility = 0
    grid = grid.split('\n')
    gridHeight = len(grid)
    gridWidth = len(grid[0])
    for i, row in enumerate(grid): # for every row of the grid
        for j, currTree in enumerate(row): # for every element of every row
            currTreeViewDist = checkTreeViewDist(grid, currTree, i, j, gridHeight, gridWidth)
            if currTreeViewDist > highestTreeVisibility:
                highestTreeVisibility = currTreeViewDist
    return highestTreeVisibility 

#numVisibleTrees = findVisibleTrees(data.data)
greatestVisibility = findGreatestVisibility(data.data)
print(greatestVisibility)

