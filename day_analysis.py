import sys
from idk import *
from seven_to_fourteen import *
from roles_shells import *

from day_vote_exp import *


def who_to_hang():
    global person_to_kill
    votes_values = []
    candidates_to_hang = []
    for k in blya.all_vars:
        votes_values.append(k.votes)
    max_value = max(votes_values)
    for k in blya.all_vars:
        if k.votes == max_value:
            candidates_to_hang.append(k)
    return random.choice(candidates_to_hang)




def check_for_win():
    counter_mir = 0
    counter_death = 0
    for k in blya.all_vars:
        if k.role != 'Oprich' and k.status == 'alive':
            counter_mir += 1
        if k.role == 'Oprich' and k.status == 'alive':
            counter_death += 1
    if counter_death >= counter_mir:
        return ('оприч выиграли')
    elif counter_death == 0:
        return ('мир выиграл')

def obnulenie():
    for i in blya.all_vars:
        if i.blocked == True:
            i.blocked = False
        if i.healed == True:
            i.healed = False

