id = 0

class Cell:
    def __init__(self):
        global id

        self.id = id+1
        self.dir = 'FORWARD'
        self.next = None

        id += 1

    def add(self, cell):
        if self.next:
            self.next.add(cell)
        else:
            self.next = cell

    def move_adjacent_accordingly(self):
        if self.dir == 'LEFT':
            self.next.left()

        elif self.dir == 'RIGHT':
            self.next.right()

        elif self.dir == 'FORWARD':
            self.next.forward()

    def left(self):
        print(f'{self.id} Moving left')

        if self.next:
            print('have next, moving next accordingly')
            self.move_adjacent_accordingly()
        else:
            print('dont have next')
        self.dir = 'LEFT'
        print(f'{self.id} Moved left')

    def right(self):
        print(f'{self.id} Moving right')
        
        if self.next:
            print('have next, moving next accordingly')
            self.move_adjacent_accordingly()
        else:
            print('dont have next')
        self.dir = 'RIGHT'
        print(f'{self.id} Moved right')

    def forward(self):
        print(f'{self.id} Moving forward')
        
        if self.next:
            print('have next, moving next accordingly')
            self.move_adjacent_accordingly()
        else:
            print('dont have next')
        self.dir = 'FORWARD'
        print(f'{self.id} Moved forward')



class Snake:
    def __init__(self, length=3):
        self.head = Cell()

        for i in range(length-1):
            self.grow()

    def grow(self):
        cell = Cell()
        self.head.add(cell)
    
    def move_left(self):
        self.head.left()

    def move_right(self):
        self.head.right()

    def move_forward(self):
        self.head.forward()


if __name__ == "__main__":
    snake = Snake()

    # cell = snake.head
    # while cell:
    #     print(cell.id, cell.dir)

    #     cell = cell.next

    while True:
        cmd = int(input('Enter command: '))

        if cmd == 4:
            snake.move_left()

        elif cmd == 6:
            snake.move_right()

        elif cmd == 5:
            snake.grow()

        else:
            snake.move_forward()
