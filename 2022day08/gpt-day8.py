import data
def count_visible_trees(grid):
    rows = len(grid)
    cols = len(grid[0])
    visible_trees = 0

    for i in range(rows):
        for j in range(cols):
            height = int(grid[i][j])

            # Check if the current tree is on the edge
            on_edge = i == 0 or i == rows - 1 or j == 0 or j == cols - 1

            # Initialize variables to check visibility in each direction
            visible_left = True
            visible_right = True
            visible_up = True
            visible_down = True

            # Check visibility to the left
            for x in range(j - 1, -1, -1):
                if int(grid[i][x]) >= height:
                    visible_left = False
                    break

            # Check visibility to the right
            for x in range(j + 1, cols):
                if int(grid[i][x]) >= height:
                    visible_right = False
                    break

            # Check visibility upward
            for y in range(i - 1, -1, -1):
                if int(grid[y][j]) >= height:
                    visible_up = False
                    break

            # Check visibility downward
            for y in range(i + 1, rows):
                if int(grid[y][j]) >= height:
                    visible_down = False
                    break

            # If the tree is on the edge or visible from at least one direction, count it
            if on_edge or (visible_left or visible_right or visible_up or visible_down):
                visible_trees += 1

    return visible_trees

# Input grid as a list of strings
grid = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390"
]
splitInputData = data.data.split("\n")
result = count_visible_trees(splitInputData)
print(f"Number of visible trees: {result}")

