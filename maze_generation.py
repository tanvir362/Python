import sys
import random
from colorama import init, Fore

init()

PASSAGE = 'P'
BLOCKED = 'B'
grid = {}


def calculate_frontier_cells(cell, state=BLOCKED):
    x, y = cell
    ftr_cells = []
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        f_cell = (x+dx, y+dy)
        if grid.get(f_cell):
            if grid[f_cell] == state:
                ftr_cells.append(f_cell)

    return ftr_cells

def print_maze():
    for i in range(h):
        for j in range(w):
            if grid[(j, i)]==BLOCKED:
                print(Fore.BLACK, '#', end='')
            elif grid[(j, i)]==PASSAGE:
                print(Fore.GREEN, '0', end='')
                
        
        print()
    
    print('-'*w)



h, w = map(int, sys.argv[1:3])

for i in range(h):
    for j in range(w):
        grid[(j, i)] = BLOCKED

x = random.randint(0, w-1)
y = random.randint(0, h-1)

grid[(x, y)] = PASSAGE

frontier_cells = calculate_frontier_cells((x, y))
while frontier_cells:
    rand_idx = random.randint(0, len(frontier_cells)-1)
    cell = frontier_cells.pop(rand_idx)

    grid[cell] = PASSAGE
    frontier_passages = calculate_frontier_cells(cell, PASSAGE)
    target_passage = random.choice(frontier_passages)
    dx, dy = (target_passage[0]-cell[0])//2, (target_passage[1]-cell[1])//2
    grid[(cell[0]+dx, cell[1]+dy)] = PASSAGE

    frontier_cells.extend(calculate_frontier_cells(cell))
    
    # print_maze()

print_maze()





