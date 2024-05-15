from idk import *
from seven_to_fourteen import *
from roles_shells import *
print(roles_dict)
def voting(): #все голосование
    voting_list = {}
    candidates = []
    def voting_itself (x): #непосредственно голоса
        print ('Голосует ' + x)
        vote = input()
        if vote not in voting_list:
            voting_list[vote] = 1
        else:
            voting_list[vote] += 1
    print(a)
    def find_candidates(x): #найти кандидатов с бОльшим кол-вом голосов
        for i in range (len(a)):
            voting_itself(a[i])
        print(voting_list)
        maxi = 0
        for key, value in voting_list.items():
            if value >= maxi:
                maxi = value
        for key, value in voting_list.items():
            if value == maxi:
                candidates.append(key)
        print(candidates)
        if len(candidates) == 1:
            print('Горожане казнили ' + candidates[0])
            for j in range (len(candidates)):
                if type(roles_dict.setdefault(candidates[j])) == Boyar:
                    print('Выберите, кому оставить наследство')
                    inherit(input())       
        else:
            voting_list = {}
            candidates = ','.join(candidates)
            print('Пожалуйста, выберите между этими кандидатами: ' + candidates)
            candidates = []
            for i in range (len(a)):
                voting_itself(a[i])
            print(voting_list)
            maxi = 0
            for key, value in voting_list.items():
                if value >= maxi:
                    maxi = value
            for key, value in voting_list.items():
                if value == maxi:
                    candidates.append(key)
            candidates = ','.join(candidates)
            print('Горожане казнили: ' + candidates)
        def boyar_checker(): #проверить роли казненных и оставить иммунитет
            find_candidates(candidates)
            for j in range (len(candidates)):
                if type(roles_dict.setdefault(candidates[j])) == Boyar:
                    print('Выберите, кому оставить наследство')
                    input().immun = True                
        
voting()    