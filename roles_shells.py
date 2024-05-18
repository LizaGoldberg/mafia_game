import random


class Player(object):
    status = 'alive'
    blocked = False
    healed = False
    immun = False
    immun_ability = False
    votes = 0
    def __init__(self, name):
        self.name = name
    def role_name(self, role):
        self.role = role
        print('player' + role)
    def set_blocked(self):
        self.blocked = True
    def set_healed(self):
        self.healed = True
    def set_status(self):
        self.status = 'dead'
    def to_vote(self):
        self.votes += 1
    def check_if_killable(self):
        if self.healed is False and self.immun is False:
            self.status = 'dead'
            print('опричники убили '+ Player.role)
        else:
            print('опричники хотела убить '+ Player.role + ', но не смогла')
    # def to_click(self):

class Healer(Player):
    already_healed = None
    role = 'Healer'
    def to_heal(self, a):
        a.healed = True
        self.already_healed = a.name



class GirlX(Player):
    role = "GirlX"
    def to_block(self, a):
        a.blocked = True


class Oprich(Player):
    role = 'Oprich'
    def to_kill(self, a, b):
        b.append(a.role_name)



class Priest(Player):
    role = 'Priest'
    def active_or_not(self, a):
        if a.role != 'Peasant':
            print('активна')
        else:
            print('лох педальный')


class Peasant(Player):
    role = 'Peasant'
    pass


class Dyak(Player):
    role = 'Dyak'
    def find_what_role(self, a):
        print(a.role)



class Boyar(Player):
    role = 'Boyar'
    def inherit(self, a):
        a.immun_ability = True


def candidate_to_kill(b):
    global person_to_kill
    # d = set(b)
    # c = {}
    # for i in d:
    #     c[i] = 0
    # for i in b:
    #     for k in c.keys:
    #         if i == k:
    #             c[k] += 1
    # c = dict(sorted(c.items(), key=lambda item: item[1]))
    if len(b) == 1:
        person_to_kill = b[0]
    else:
        if b[0] == b[1]:
            person_to_kill = b[0]
        else:
            person_to_kill = random.choice(b)


counter = 0

def boyar_dead(a):
    gavna = 0
    for i in a:
        if i.role == 'Boyar' and i.status == 'dead':
            gavna += 1
            if gavna < 3:
                for k in a:
                    if k.immun_ability is True:
                        k.immun = True



# def what_to_show(a):
#     for i in all_vars:
#         if a == i.name and a == 'Peasant':
#             print(random(phrases_for_peasant))
#             # button ok



