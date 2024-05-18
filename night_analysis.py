import sys
from idk import *
from seven_to_fourteen import *
from roles_shells import *
from night_vote_exp import *
from day_vote_exp import *


def actual_kill():
    global person_to_kill
    for i in blya.aa:
        if i.name == person_to_kill:
            i.check_if_killable()

def check_for_win():
    counter_mir = 0
    counter_death = 0
    for k in blya.all_vars:
        if k.role != 'Oprich' and k.status == 'alive':
            counter_mir += 1
        if k.role == 'Oprich' and k.status == 'alive':
            counter_death += 1
    if counter_death >= counter_mir:
        print('оприч выиграли')
    elif counter_death == 0:
        print('мир выиграл')



def obnulenie():
    for i in blya.all_vars:
        if i.blocked == True:
            i.blocked = False
        if i.healed == True:
            i.healed = False

