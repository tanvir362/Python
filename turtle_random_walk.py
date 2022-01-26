import turtle as tl
import random
import time

STEP_LENGTH = 30
tl.speed(1)
tl.left(90)

def walk1():
    for i in range(1000):
        angle = random.randrange(0, 360, 45)
        # print(turn)
        # if turn == 0:
        #     tl.forward(STEP)
        # elif turn == 1:
        #     tl.left(90)
        #     tl.forward(STEP)
        # elif turn == 2:
        #     tl.backward(STEP)
        # else:
        #     tl.right(90)
        #     tl.forward(STEP)


        step = 'forward' if angle<=90 or angle>=270 else 'backward'
        turn = 'left' if angle<=90 or (angle>=180 and angle<270) else 'right'

        if turn == 'left':
            angle = angle if angle<180 else (angle-180)
        else:
            angle = (360-angle) if angle>=270 else (angle-90)
        
        if turn == 'left':
            tl.left(angle)
        else: tl.right(angle)

        print(turn, step, angle)
        time.sleep(0.5)

        if step == 'forward':
            tl.forward(STEP_LENGTH)
        else: tl.backward(STEP_LENGTH)


if __name__ == "__main__":
    walk1()
