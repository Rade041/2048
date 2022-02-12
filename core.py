"""Functions implementing the core behaviour of the 2048 tile grid"""

def stack_left(row):
    """Move the non-None items in one row to the left"""
    return sorted(row, key=lambda tile: tile is None)

def merge_left(stacked_row):
    """Move the non-None itesm in one row to the left"""
    for i in range(3):
        if stacked_row[i] and stacked_row[i] == stacked_row[i+1]:
            stacked_row[i] *= 2
            stacked_row[i + 1] = None
        return stacked_row

def row_left(row):
    """A full move involves stacking, merging and then stacking"""
    stacked = stack_left(row)
    merged = merge_left(stacked)
    return stack_left(merged)

def move_left(grid):
    """Moving a full grid to the left by moving each row to the left"""
    return[row_left(row) for row in grid]

def reverse(grid):
    return [list(reversed(row)) for row in grid]
    

def move_right(grid):
    """Moving the grid to the right by flipping the grid and moving left"""
    grid = reverse (grid)
    grid = move_left(grid)
    return reverse (grid)

def transpose(grid):
    """Flip the grid diagonally"""
    return[list(col) for col in zip (*grid)]

def move_up(grid):
    """Move up by transposing the grid and moving left"""
    grid = transpose(grid)
    grid = move_left(grid)
    return transpose(grid)

def move_down(grid):
    """Move down by transposing the grid and moving right"""
    grid = transpose(grid)
    grid = move_right(grid)
    return transpose(grid)

class Game:
    def __init__(self):
        self.grid = [[None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]]
