import turtle as tl
import random
import time

STEP_LENGTH = 40
X_MIN = -2
X_MAX = 2
Y_MIN = -2
Y_MAX = 2
all_options = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = {}

# tl.right(135)
# tl.speed(1)
tl.hideturtle()

def valid_point(x, y):
    return (x>=X_MIN and x<=X_MAX) and (y>=Y_MIN and y<=Y_MAX)


direction = {
    (1, 0) : "right",
    (0, 1) : "up",
    (-1, 0) : "left",
    (0, -1) : "down"
}

# tl.goto(67*STEP_LENGTH, 33*STEP_LENGTH)



# def walk_from(x, y):
#     options = []
#     for dx, dy in all_options:
#         if valid_point(x+dx, y+dy):
#             if not table[(x+dx, y+dy)]:
#                 options.append((dx, dy))
#     random.shuffle(options)

#     while len(options):
#         # print(f'available options: {", ".join(map(lambda x: direction[x], options))}')
#         dx, dy = options.pop(0)
#         # tl.pendown()
#         tl.color('black')
#         tl.goto((x+dx)*STEP_LENGTH, (y+dy)*STEP_LENGTH)
#         # print(direction[(dx, dy)], f"from {(x, y)}")
#         # time.sleep(10)
#         table[(x+dx, y+dy)] = True
#         walk_from(x+dx, y+dy)
#         if sum(1 for v in table.values() if v==False)==0:
#             raise Exception('All point touched')
#         table[(x+dx, y+dy)] = False
#         # print(f"back at {(x, y)}")
#         # tl.penup()
#         tl.color('white')
#         tl.goto(x*STEP_LENGTH, y*STEP_LENGTH)
#         # time.sleep(10)

def get_available_options(x, y):
    options = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    available = []
    
    for dx, dy in options:
        if valid_point(x+dx, y+dy):
            if not visited[(x+dx, y+dy)]:
                available.append((dx, dy))

    return available


def walk_from(x, y):
    options = get_available_options(x, y)
    random.shuffle(options)

    while options:
        dx, dy = options.pop(0)

        visited[(x+dx, y+dy)] = True
        tl.color('black')
        tl.pendown()
        tl.goto((x+dx)*STEP_LENGTH, (y+dy)*STEP_LENGTH)
        walk_from(x+dx, y+dy)

        if sum(1 for is_visited in visited.values() if is_visited == False) == 0:
            break
        
        visited[(x+dx, y+dy)] = False
        tl.color('white')
        tl.goto(x*STEP_LENGTH, y*STEP_LENGTH)


def walk_from1(x, y):
    options = get_available_options(x, y)
    random.shuffle(options)

    while options:
        dx, dy = options.pop(0)

        visited[(x+dx, y+dy)] = True
        tl.goto((x+dx)*STEP_LENGTH, (y+dy)*STEP_LENGTH)
        walk_from1(x+dx, y+dy)

        if sum(1 for is_visited in visited.values() if is_visited == False) == 0:
            tl.pendown()
            tl.goto(x*STEP_LENGTH, y*STEP_LENGTH)
            break
        
        visited[(x+dx, y+dy)] = False





def start_walk(x, y):
    visited[(x, y)] = True
    tl.penup()
    tl.goto(x*STEP_LENGTH, y*STEP_LENGTH)
    # tl.pendown()tl.dot(5)
    walk_from1(x, y)
    # try:
    # except Exception as e:
    #     print(str(e))

def setup():
    tl.penup()
    for x in range(X_MIN, X_MAX+1, 1):
        for y in range(Y_MIN, Y_MAX+1, 1):
            tl.goto(x*STEP_LENGTH, y*STEP_LENGTH)
            tl.dot()
            visited[(x, y)] = False

    # tl.pendown()

setup()
start_walk(0, 0)

tl.exitonclick()