from idk import *
from seven_to_fourteen import *
from roles_shells import *
print(roles_dict)
def voting():
    voting_list = {}
    global candidates    
    candidates = []
    def voting_itself (x): #непосредственно голосование
        if (roles_dict.setdefault(x)).blocked == False:
            print ('Голосует ' + x)
            vote = input()
            if vote not in voting_list:
                voting_list[vote] = 1
            else:
                voting_list[vote] += 1
    print(a)
    for i in range (len(a)):
        voting_itself(a[i])
    print(voting_list)
    def find_candidates (): #найти кандидатов
        maxi = 0
        for key, value in voting_list.items(): 
            if value >= maxi:
                maxi = value
        for key, value in voting_list.items():
            if value == maxi:
                candidates.append(key)
        print(candidates)
    find_candidates()
    if len(candidates) == 1:
        def exec1(): #казнить одного
            print('Горожане казнили ' + candidates[0]) 
        exec1()
        for j in range (len(candidates)):
                if type(roles_dict.setdefault(candidates[j])) == Boyar:
                    boyarin = roles_dict.setdefault(candidates[j])
                    def boyar_function(): #функция боярина
                        print(candidates[j] + ', выберите, кому оставить наследство')  
                        name = input()
                        boyarin.inherit(roles_dict.setdefault(name))
                        print(roles_dict.setdefault(name).immun)
                    boyar_function()
        def kick(): #удалить игрока
            a.remove(candidates[0]) 
            del roles_dict[candidates[0]]
            print(roles_dict)
        kick()
    else:
        def exec_many(): #казнить нескольких
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
        exec_many()
        for j in range (len(candidates)):
            if type(roles_dict.setdefault(candidates[j])) == Boyar:
                boyarin = roles_dict.setdefault(candidates[j])
                boyar_function()
        for b in range(len(candidates)):
            kick(b)
        for b in range(candidates):
            null(candidates(b))
    def null(): #обнуление
        for b in range (len(a)): 
            (roles_dict.setdefault(a[b])).blocked = False
            (roles_dict.setdefault(a[b])).healed = False
    null()
    def victory(x): #определяем, закончилась ли игра и в чью пользу
        op = 0
        pe = 0
        for v in range (len(a)):
            if type(roles_dict.setdefault(a[v])) == Oprich or type(roles_dict.setdefault(a[v])) == Tsar or type(roles_dict.setdefault(a[v])) == Maluta:
                op += 1
            else:
                pe += 1
        if op >= pe:
            print('Игра закончена, победили опричники')
        elif op == 0:
            print('Игра закончена, победили мирные жители')
        #else:
            #print('Продолжаем')
    victory(a)       
voting()    
