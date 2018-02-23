grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

grid2 = []
y = 0
def print_line(grid):
    new_list = []
    for x in range(len(grid)):
        new_line = grid[x][y]
        new_list.append(new_line)
    return new_list

for y in range(5):
    new_line = print_line(grid)
    grid2.append(new_line)

for i in range(len(grid2)):
    print ''.join(map(str,grid2[i]))
