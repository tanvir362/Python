import sys

class Factory:
    def __init__(self, id):
        self.id = id
        self.links = {}

    def set_params(self, owner, cyborg_count, production_capacity):
        self.owner = owner
        self.cyborg_count = cyborg_count
        self.production_capacity = production_capacity

    
    def cyborg_needs_to_conquer(self):
        enemy_reaching = sum(troop.cyborg_count for troop in game.enemy_troops if troop.target==self.id)
        # print(f'id: {self.id}\nenemy reaching {enemy_reaching}', file=sys.stderr, flush=True)

        mine_reaching = sum(troop.cyborg_count for troop in game.my_troops if troop.target==self.id)
        # print(f'mine reaching {mine_reaching}', file=sys.stderr, flush=True)

        need = enemy_reaching - mine_reaching

        if self.owner == 1:
            need -= self.cyborg_count
            # print(f'mine in factory {self.cyborg_count}\nneed: {need}', file=sys.stderr, flush=True)

        else:
            need += self.cyborg_count + self.production_capacity
            # print(f'enemy in factory {self.cyborg_count + self.production_capacity}\nneed: {need}', file=sys.stderr, flush=True)

        need += 3
        self.conquer_needs = need
        return need



class Troop:
    def __init__(self, id, owner, source, target, cyborg_count, dist_remain):
        self.id = id
        self.owner = owner
        self.source = source
        self.target = target
        self.cyborg_count = cyborg_count
        self.dist_remain = dist_remain


class Game:
    def __init__(self):
        self.factories = []
        self.my_troops = []
        self.enemy_troops = []
        self.bomb_available = 2

    def add_troop(self, troop):
        if troop.owner == 1:
            self.my_troops.append(troop)
        else:
            self.enemy_troops.append(troop)

    def get_my_factories(self, ids=None):
        # return filter(lambda x: x.owner==1, self.factories)
        if ids:
            factories = [factory for factory in self.factories if factory.owner==1 and factory.id in ids]
        else:
            factories = [factory for factory in self.factories if factory.owner==1]

        return factories

    def get_enemy_factories(self):
        factories = [factory for factory in self.factories if factory.owner==-1]

        return factories

    def get_factory(self, id):
        # factory = filter(lambda x: x.id==id, self.factories)
        factory = [factory for factory in self.factories if factory.id == id]

        if factory:
            factory = factory[0]
        else:
            factory = Factory(id)
            self.factories.append(factory)
        
        return factory

    def empty_troops(self):
        self.enemy_troops = []
        self.my_troops = []


game = Game()

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories

for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    game.get_factory(factory_1).links[factory_2] = distance
    game.get_factory(factory_2).links[factory_1] = distance


# game loop
while True:
    game.empty_troops()
    commands = []
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        arg_1 = int(inputs[2])
        arg_2 = int(inputs[3])
        arg_3 = int(inputs[4])
        arg_4 = int(inputs[5])
        arg_5 = int(inputs[6])

        if entity_type == 'FACTORY':
            factory = game.get_factory(entity_id)
            factory.set_params(arg_1, arg_2, arg_3)
        elif entity_type == 'TROOP':
            troop = Troop(entity_id, arg_1, arg_2, arg_3, arg_4, arg_5)
            game.add_troop(troop)

        # elif entity_type == 'BOMB':
        #     owner, source, target, rem = arg_1, arg_2, arg_3, arg_4
        #     my_facts = game.get_my_factories()
        #     if len(my_facts)>=2:
        #         my_facts = sorted(my_facts, key=lambda x: x.cyborg_count)
        #         commands.append(f'MOV {my_facts[-1].id} {my_facts[0].id} {my_facts[0].cyborg_count}')
        #         my_facts[-1].cyborg_count = 0


    game.factories = sorted(game.factories, key=lambda x: (x.cyborg_needs_to_conquer(), -x.production_capacity), reverse=False)
    
    if game.bomb_available == 2:
        commands.append(f'BOMB {game.get_my_factories()[0].id} {game.get_enemy_factories()[0].id}')
        game.bomb_available -= 1
    for fact in game.factories:
        print(f"factory id: {fact.id} conquer_needs: {fact.conquer_needs}", file=sys.stderr, flush=True)
        if fact.conquer_needs <= 0: continue

        for link in sorted(fact.links.keys(), key=lambda x: fact.links[x]):
            link_fact = game.get_factory(link)
            # print(f"link: {link_fact.id} owner: {link_fact.owner} cyborg count: {link_fact.cyborg_count} dist: {fact.links[link]}", file=sys.stderr, flush=True)

            is_troop_sent = False
            if link_fact.cyborg_count > fact.conquer_needs and link_fact.owner == 1:
                commands.append(f'MOVE {link_fact.id} {fact.id} {fact.conquer_needs}')
                link_fact.cyborg_count -= fact.conquer_needs
                link_fact.cyborg_count = max(0, link_fact.cyborg_count)
                is_troop_sent = True
            
            if is_troop_sent:
                break
                
    print(';'.join(commands), file=sys.stderr, flush=True)
    if not commands:
        if game.bomb_available:
            bomb_fact = sorted(game.get_enemy_factories(), key=lambda x: x.cyborg_count)[-1]

            bomb_sent = False
            for link in sorted(bomb_fact.links.keys(), key=lambda x: bomb_fact.links[x]):
                link_fact = game.get_factory(link)
                if link_fact.owner == 1 and len([troop for troop in game.enemy_troops if troop.source == link_fact.id])==0:
                    print(f'BOMB {link_fact.id} {bomb_fact.id}')
                    game.bomb_available -= 1
                    bomb_sent = True
                    break

            if not bomb_sent: print("WAIT")
        else: print("WAIT")
    else:
        print(';'.join(commands))
