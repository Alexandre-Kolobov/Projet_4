#separer dans des differrents fichiers
class Tournament:
    def __init__(self, name, place, date_start, date_finish = "", round_all = 4, round_current = "", description  = ""):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_finish = date_finish
        self.round_current = round_current
        self.round_list = []
        self.players_list = []
        self.description = description
        self.round_all = round_all

    def add_player(self, player):
        self.players_list.append(player)

    #add player
    #add round
