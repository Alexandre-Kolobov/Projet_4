class Tournament:
    def __init__(self, name, place, date_start, date_finish = "", round_all = 4, round_current = "", round_list  = [], players_list  = [], description  = ""):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_finish = date_finish
        self.round_current = round_current
        self.round_list = round_list
        self.players_list = players_list
        self.description = description
        self.round_all = round_all

class Round(Tournament):
    def __init__(self, name, games = [], date_start = "", date_finish = ""):
        self.name = name
        self.games = games
        self.date_start = date_start
        self.date_finish = date_finish

    def __repr__(self):
        return f"{self.name}"

class Game(Round):
    def __init__(self, player_1, score_1, player_2, score_2):
        self.game = ([player_1, score_1], [player_2, score_2])

    def __repr__(self):
        return f"{self.game}"