class Tournament:
    def __init__(self, name, place, date_start, date_finish = "", round_all = "4", round_current = "", round_list  = [], players_list  = [], description  = ""):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_finish = date_finish
        self.round_current = round_current
        self.round_list = round_list
        self.players_list = players_list
        self.description = description
        self.round_all = round_all

    def round_estimation(self):
        pass

class Round(Tournament):
    def __init__(self, name, date_start, date_finish):
        pass

class Game(Round):
    def __init__(self, player_1, score_1, player_2, score_2):
        self.game = ([player_1, score_1], [player_2, score_2])

