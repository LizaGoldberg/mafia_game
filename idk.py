import random
from seven_to_fourteen import *

print('колво игроков от 7 до 14')
n = int(input())
with open('roles.txt', 'r') as f:
    i = 0
    b = []
    while i < n:
        b.append(f.readline().strip())
        i = i+1

print(b)
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
print(c)

if n >= 7:
    player1 = None
    player1 = what_role(a, 0, player1, c)
    roles_dict[a[0]] = player1
    player2 = None
    player2 = what_role(a, 1, player2, c)
    roles_dict[a[1]] = player2
    player3 = None
    player3 = what_role(a, 2, player3, c)
    roles_dict[a[2]] = player3
    player4 = None
    player4 = what_role(a, 3, player4, c)
    roles_dict[a[3]] = player4
    player5 = None
    player5 = what_role(a, 4, player5, c)
    roles_dict[a[4]] = player5
    player6 = None
    player6 = what_role(a, 5, player6, c)
    roles_dict[a[5]] = player6
    player7 = None
    player7 = what_role(a, 6, player7, c)
    roles_dict[a[6]] = player7
    if n >=8:
        player8 = None
        player8 = what_role(a, 7, player8, c)
        roles_dict[a[7]] = player8
        if n >= 9:
            player9 = None
            player9 = what_role(a, 8, player9, c)
            roles_dict[a[8]] = player9
            if n >= 10:
                player10 = None
                player10 = what_role(a, 9, player10, c)
                roles_dict[a[9]] = player10
                if n >=11:
                    player11 = None
                    player11 = what_role(a, 10, player11, c)
                    roles_dict[a[10]] = player11
                    if n >=12:
                        player12 = None
                        player12 = what_role(a, 11, player12, c)
                        roles_dict[a[11]] = player12
                        if n >= 13:
                            player13 = None
                            player13 = what_role(a, 12, player13, c)
                            roles_dict[a[12]] = player13
                            if n ==14:
                                player14 = None
                                player14 = what_role(a, 13, player14, c)
                                roles_dict[a[13]] = player14
print(player1.name)



