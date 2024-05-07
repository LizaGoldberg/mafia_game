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

#вводим кол-во игроков, на основе этого вычленяем нужную часть ролей из roles.txt, получившийся список ролей шаффлим

random.shuffle(b)
a = []
c = {}
i = 0
while i < n:
    print('введи имя')
    d = str(input())
    a.append(d)
    print('роль:', b[i])
    c[str(d)] = str(b[i])
    i = i + 1
# игроки вводят свое имя, сразу же назначается роль из зашаффленного списка

if n >= 7:
    player1 = None
    player1 = what_role(a, 0, player1, c)
    player2 = None
    player2 = what_role(a, 1, player2, c)
    player3 = None
    player3 = what_role(a, 2, player3, c)
    player4 = None
    player4 = what_role(a, 3, player4, c)
    player5 = None
    player5 = what_role(a, 4, player5, c)
    player6 = None
    player6 = what_role(a, 5, player6, c)
    player7 = None
    player7 = what_role(a, 6, player7, c)
    if n >=8:
        player8 = None
        player8 = what_role(a, 7, player8, c)
        if n >= 9:
            player9 = None
            player9 = what_role(a, 8, player9, c)
            if n >= 10:
                player10 = None
                player10 = what_role(a, 9, player10, c)
                if n >=11:
                    player11 = None
                    player11 = what_role(a, 10, player11, c)
                    if n >=12:
                        player12 = None
                        player12 = what_role(a, 11, player12, c)
                        if n >= 13:
                            player13 = None
                            player13 = what_role(a, 12, player13, c)
                            if n ==14:
                                player14 = None
                                player14 = what_role(a, 13, player14, c)

#это цикл для создания переменных (игрок+роль+класс)


