import random

class Player(object):
    status = 'alive'
    blocked = False
    healed = False
    def __init__(self, name):
        self.name = name
    def role_name(self, role):
        print('player')
        self.role = role
    def set_blocked(self, blocked):
        self.blocked = True
    def set_healed(self, healed):
        self.healed = True
    def set_status(self, status):
        self.status = 'dead'

class Healer(Player):
    def role_name(self, role):
        Player.role = 'Healer'
        print('healer')
    def to_heal(self, Player):
        Player.healed = True

class GirlX(Player):
    def role_name(self, role):
        Player.role = 'GirlX'
        print('girl')
    def to_block(self, Player):
        Player.blocked = True

class Oprich(Player):
    def role_name(self, role):
        Player.role = 'Oprich'
        print('oprich')
    def to_kill(self, Player):
        Player.status = 'dead'

class Priest(Player):
    pass

class Tsar(Player):
    pass

class Maluta(Player):
    pass

class Peasant(Player):
        def role_name(self, role):
            Player.role = 'Peasant'
            print('peasant')

class Maluta(Player):
    pass

class Dyak(Player):
    pass

class Boyar(Player):
    pass




