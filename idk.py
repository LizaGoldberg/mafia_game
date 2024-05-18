import sys
import random
from seven_to_fourteen import *
from roles_shells import *

print('колво игроков от 7 до 12')
n = int(input())
with open('roles.txt', 'r') as f:
    i = 0
    b = []
    while i < n:
        b.append(f.readline().strip())
        i = i+1

random.shuffle(b)
a = []
c = {}
roles_dict = {}
i = 0
while i < n:
    print('введи имя')
    d = str(input())
    a.append(d)
    print('роль:', b[i])
    c[str(d)] = str(b[i])
    i = i + 1

all_vars = []

class blya():
    def __init__(self):
        super().__init__()
        self.nn = None
        self.aa = None
        self.all_vars = None
        self.name_clicked = None
        self.max_alive = None


blya.nn = n
blya.aa = a

if n >= 7:
    player1 = None
    player1 = what_role(a, 0, player1, c)
    all_vars.append(player1)
    roles_dict[a[0]] = player1
    player2 = None
    player2 = what_role(a, 1, player2, c)
    all_vars.append(player2)
    roles_dict[a[1]] = player2
    player3 = None
    player3 = what_role(a, 2, player3, c)
    all_vars.append(player3)
    roles_dict[a[2]] = player3
    player4 = None
    player4 = what_role(a, 3, player4, c)
    all_vars.append(player4)
    roles_dict[a[3]] = player4
    player5 = None
    player5 = what_role(a, 4, player5, c)
    all_vars.append(player5)
    roles_dict[a[4]] = player5
    player6 = None
    player6 = what_role(a, 5, player6, c)
    all_vars.append(player6)
    roles_dict[a[5]] = player6
    player7 = None
    player7 = what_role(a, 6, player7, c)
    all_vars.append(player7)
    roles_dict[a[6]] = player7
    if n >=8:
        player8 = None
        player8 = what_role(a, 7, player8, c)
        all_vars.append(player8)
        roles_dict[a[7]] = player8
        if n >= 9:
            player9 = None
            player9 = what_role(a, 8, player9, c)
            all_vars.append(player9)
            roles_dict[a[8]] = player9
            if n >= 10:
                player10 = None
                player10 = what_role(a, 9, player10, c)
                all_vars.append(player10)
                roles_dict[a[9]] = player10
                if n >=11:
                    player11 = None
                    player11 = what_role(a, 10, player11, c)
                    all_vars.append(player11)
                    roles_dict[a[10]] = player11
                    if n >=12:
                        player12 = None
                        player12 = what_role(a, 11, player12, c)
                        all_vars.append(player12)
                        roles_dict[a[11]] = player12

blya.all_vars = all_vars

