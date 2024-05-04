from roles_shells import *


def what_role(people, i, person, some_roles):
    print(some_roles[people[i]])
    if some_roles[people[i]] == 'Oprich':
        person = Oprich(Player)
        person.name = people[i]
    elif some_roles[people[i]] == 'Healer':
        person = Healer(Player)
        person.name = people[i]
    elif some_roles[people[i]] == 'GirlX':
        person = GirlX(Player)
        person.name = people[i]
    elif some_roles[people[i]] == 'Dyak':
        person = Dyak(Player)
        person.name = people[i]
    elif some_roles[people[i]] == 'Peasant':
        person = Peasant(Player)
        person.name = people[i]
    elif some_roles[people[i]] == 'Boyar':
        person = Boyar(Player)
        person.name = people[i]
    elif some_roles[people[i]] == 'Tsar':
        person = Tsar(Player)
        person.name = people[i]
    elif some_roles[people[i]] == 'Maluta':
        person = Maluta(Player)
        person.name = people[i]
    elif some_roles[people[i]] == 'Priest':
        person = Priest(Player)
        person.name = people[i]
    return person





