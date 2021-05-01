class Cell:
    def __init__(self, tail=None, curr_head_dir=None, next_head_dir=None):
        self.tail = tail
        self.curr_head_dir = curr_head_dir
        self.next_head_dir = next_head_dir
    
    def move(self, dir=None):
        if dir: #dir will only be pass for first cell
            print(dir)
            if self.tail:
                self.tail.next_head_dir = dir
        else:
            print(self.curr_head_dir)
            if self.tail:
                self.tail.next_head_dir = self.curr_head_dir
            self.curr_head_dir = self.next_head_dir


class Snake:
    def __init__(self):
        self.first_cell = Cell()
    
    def grow(self):
        current = self.first_cell
        while current.tail:
            current = current.tail
        
        new_cell = Cell(curr_head_dir=2)
        current.tail = new_cell
    
    def move(self, dir=None):
        if dir:
            self.first_cell.move(dir)
            current = self.first_cell.tail
            while current:
                current.move()
                current = current.tail
        else:
            current = self.first_cell
            while current:
                current.move(2)
                current = current.tail

    def initial(self):
        print('initial')
        current = self.first_cell.tail
        while current:
            current.curr_head_dir = 2
            current.next_head_dir = None
            current = current.tail
