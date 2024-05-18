from mafia.seven_to_fourteen import what_role


class blya():
    name_clicked = None
    max_alive = None

    def __init__(self):
        super().__init__()
        self.name_clicked = None
        self.max_alive = None


def get_number_players():
    global number_players
    return number_players


def get_names_players():
    global names_players
    return names_players


def get_roles_players():
    global roles_players
    return roles_players


def append_names_players(m):
    global names_players
    names_players.append(m)


def set_roles_players(m):
    global roles_players
    roles_players = m


def set_number_players(n):
    global number_players
    number_players = n


def set_all_vars():
    global all_vars
    n = get_number_players()
    #print("hi")
    #print(n)
    a = get_names_players()
    #print(a)
    c = create_dict()
    #print(c)
    if n >= 7:
        player1 = None
        player1 = what_role(a, 0, player1, c)
        all_vars.append(player1)
        player2 = None
        player2 = what_role(a, 1, player2, c)
        all_vars.append(player2)
        player3 = None
        player3 = what_role(a, 2, player3, c)
        all_vars.append(player3)
        player4 = None
        player4 = what_role(a, 3, player4, c)
        all_vars.append(player4)
        player5 = None
        player5 = what_role(a, 4, player5, c)
        all_vars.append(player5)
        player6 = None
        player6 = what_role(a, 5, player6, c)
        all_vars.append(player6)
        player7 = None
        player7 = what_role(a, 6, player7, c)
        all_vars.append(player7)
        if n >= 8:
            player8 = None
            player8 = what_role(a, 7, player8, c)
            all_vars.append(player8)
            if n >= 9:
                player9 = None
                player9 = what_role(a, 8, player9, c)
                all_vars.append(player9)
                if n >= 10:
                    player10 = None
                    player10 = what_role(a, 9, player10, c)
                    all_vars.append(player10)
                    if n >= 11:
                        player11 = None
                        player11 = what_role(a, 10, player11, c)
                        all_vars.append(player11)
                        if n >= 12:
                            player12 = None
                            player12 = what_role(a, 11, player12, c)
                            all_vars.append(player12)

def get_all_vars():
    global all_vars
    return all_vars



def create_dict():
    c = {}
    for i in range(len(get_names_players())):
        name = get_names_players()
        role = get_roles_players()
        #print("create dict")
        #print(name[i])
        #print(role[i])
        c[str(name[i])] = str(role[i])
    return c


roles_players = []
names_players = []
all_vars = []
number_players = 0
