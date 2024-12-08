#!/usr/bin/python3
'''The function island_perimeter returns the perimeter'''


def island_perimeter(grid):
    ''' Return the perimiter of an island namde Grid '''
    w = len(grid[0])
    h = len(grid)
    edge = 0
    size = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edge += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edge += 1
    return size * 4 - edge * 2
