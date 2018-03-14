tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

grid2 = []
y = 0
def printTable(tableData):
    new_list = []
    for x in range(len(tableData)):
        new_line = tableData[x][y]
        new_list.append(new_line)
    return new_list

for y in range(4):
    new_line = printTable(tableData)
    grid2.append(new_line)

for i in range(len(grid2)):
    print ' '.join(map(str,grid2[i]))
