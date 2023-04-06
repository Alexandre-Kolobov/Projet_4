#separer dans des differrents fichiers
class Tournament:
    def __init__(self, name = "", place = "", date_start = "", date_finish = "", round_all = 4, round_current = "", description  = ""):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_finish = date_finish
        self.round_current = round_current
        self.round_list = []
        self.players_list = []
        self.description = description
        self.round_all = round_all


    def modify_start_information(self, name, place, date_start):
        self.name = name
        self.place = place
        self.date_start = date_start
    
    def modify_all_round_information(self, round_all):
        self.round_all = round_all
        

    def add_player(self, player):
        self.players_list.append(player)

    def give_len_list_players(self):
        return len(self.players_list)


    def give_list_players(self):
        return self.players_list
    
    def give_round_all_information(self):
        return self.round_all

    def give_round_list(self):
        return self.round_list
    
    def add_round(self, round):
        self.round_list.append(round)

    def add_date_finish(self, date_finish):
        self.date_finish = date_finish