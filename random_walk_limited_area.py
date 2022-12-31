import turtle as tl
import random
import time

STEP_LENGTH = 10
tl.right(135)

x, y = 0, 0
# tl.goto(67*STEP_LENGTH, 33*STEP_LENGTH)

while True:
    dx , dy = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
    
    if x+dx<=67 and x+dx>=-67:
        x+=dx
    
    if y+dy<=33 and y+dy>=-32:
        y += dy

    tl.goto(x*STEP_LENGTH, y*STEP_LENGTH)


tl.exitonclick()