import random

def random_walk(n):
    x,y = 0,0

    for i in range(n):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x += dx
        y += dy

    return (x, y)

for walk_length in range(1, 31):
    walk = random_walk(walk_length)

    # print(f'Walk length: {walk_length} distance from home: {abs(walk[0])+abs(walk[1])}')
    print(f'walk length, distance - {walk_length}, {abs(walk[0])+abs(walk[1])}')
