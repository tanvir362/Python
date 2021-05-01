class Cell:
    def __init__(self, tail=None, cur_mov=2, pen_mov=None):
        self.tail = tail
        self.cur_mov = cur_mov
        self.pen_mov = pen_mov

    def move(self, dir=None):
        if dir:
            if self.tail:
                self.tail.pen_mov = self.cur_mov
            print(self.cur_mov)
            self.cur_mov = self.pen_mov
            self.pen_mov = dir
        else:
            if self.tail:
                self.tail.pen_mov = self.cur_mov
            print(self.cur_mov)
            self.cur_mov = self.pen_mov


class Snake:
    def __init__(self):
        self.first_cell = Cell()
    
    def grow(self):
        current = self.first_cell
        while current.tail:
            current = current.tail
        
        new_cell = Cell(cur_mov=current.cur_mov)
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
                current.move()
                current = current.tail

    def initial(self):
        print('initial')
        current = self.first_cell
        while current:
            current.cur_mov=2
            current = current.tail
        
        

