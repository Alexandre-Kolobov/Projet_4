class Tournament:
    def __init__(self, name, place, date_start, date_finish, round_current, round_list, players_list, description, round_all = "4"):
        pass

    def round_estimation(self):
        pass

class Round(Tournament):
    def __init__(self, name, date_start, date_finish):
        pass

class Game(Round):
    def __init__(self, player_1, score_1, player_2, score_2):
        self.game = ([player_1, score_1], [player_2, score_2])

