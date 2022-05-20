import random

class Door:
    def __init__(self, id, item):
        self.id = id
        self.inside = item
        self.state = 'CLOSED'

    @property
    def is_open(self):
        return self.state == 'OPENED'

    @property
    def is_closed(self):
        return self.state == 'CLOSED'

    @property
    def is_selected(self):
        return self.state == 'SELECTED'

    def open(self):
        self.state = 'OPENED'

    def close(self):
        self.state = 'CLOSED'

    def select(self):
        self.state = 'SELECTED'

    def __str__(self):
        return f"[{self.inside.capitalize()}]"


class MontyHall:

    def __init__(self):
        self.switched = False
        self.doors = {}

        items = ['GOAT', 'GOAT', 'CAR']
        random.shuffle(items)
        for i,v in enumerate(items):
            self.doors[i+1] = Door(i+1, v)

    
    def get_doors(self):
        return self.doors.values()

    def choose(self, choice):
        door = self.doors.get(choice)
        door.select()

        self.selected = door
        self.reveal_a_goat()

    def reveal_a_goat(self):
        doors = [d for d in self.get_doors() if (not d.is_selected) and d.inside != 'CAR']

        door = random.choice(doors)
        door.open()

        print('    '.join(map(lambda d: f"[{d.inside.capitalize() if d.is_open else [f'Door{d.id}', 'Selected'][d.is_selected]}]", self.get_doors())))

    def switch(self):
        self.switched = True

    def is_a_luck(self):
        if (self.selected.inside == 'CAR' and self.switched == False) or (self.selected.inside != 'CAR' and self.switched == True):
            return True

        return False

    def display_options(self):
        print('[Door1]    [Door2]    [Door3]')


    
if __name__ == '__main__':
    monty_hall = MontyHall()

    print('Which door do you want to select?')
    monty_hall.display_options()
    choice = int(input(': '))

    print()
    monty_hall.choose(choice)

    sw = input('Do you want to switch?(y/n)\n: ').lower()

    if sw == 'y':
        monty_hall.switch()

    print()
    print('    '.join(map(str, monty_hall.get_doors())))

    if monty_hall.is_a_luck():
        print('Congratulation, you won a sports car!')
    else:
        print('Bad luck, try again.')



