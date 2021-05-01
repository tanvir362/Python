class cell:
    def __init__(self, head=None, tail=None, face_dir=2, move_dir=None):
        self.head = head
        self.tail = tail
        self.face_dir = face_dir
        self.move_dir = move_dir
    
    def move(self, dir=None):
        if self.head:
            if self.head.face_dir == self.face_dir:
                self.move_dir = self.head.move_dir
            else:
                self.face_dir = self.head.face_dir
            
            print(self.move_dir)
            self.move_dir = self.head.move_dir
        else:
            self.face_dir = dir
            self.move_dir = dir
            print(self.move_dir)


class Snake:
    def __init__(self):
        self.head = cell()

    def add_cell(self):
        current = self.head
        while current.tail != None:
            current = current.tail
        
        new_cell = cell(head=current, face_dir=current.face_dir, move_dir=current.move_dir)
        current.tail = new_cell

    def move_up(self):
        self.head.move(1)
        current = self.head.tail
        while current:
            current.move()
            current = current.tail
    
    def move_right(self):
        self.head.move(2)
        current = self.head.tail
        while current:
            current.move()
            current = current.tail
    
    def move_down(self):
        self.head.move(3)
        current = self.head.tail
        while current:
            current.move()
            current = current.tail
    
    def move_left(self):
        self.head.move(4)
        current = self.head.tail
        while current:
            current.move()
            current = current.tail

    def print(self):
        current = self.head
        while current:
            print(f'face {current.face_dir} moved {current.move_dir}')
            current = current.tail

my_snake = Snake()
my_snake.add_cell()
my_snake.add_cell()
my_snake.move_right()
my_snake.move_right()
my_snake.move_up()
my_snake.move_right()
my_snake.move_down()
print('-------')
# my_snake.print()
