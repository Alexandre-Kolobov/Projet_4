data_path = "data\\tournaments\\"


class Match:
    def __init__(self, name, player_1, player_2, score_1=0, score_2=0):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def __repr__(self):
        return f"([{self.player_1},{self.score_1}], [{self.player_2},{self.score_2}])"

    def give_player_1(self):
        return self.player_1

    def give_player_2(self):
        return self.player_2

    def give_player_1_score(self):
        return self.score_1

    def give_player_2_score(self):
        return self.score_2

    def update_player_score(self, score_1, score_2):
        self.score_1 = score_1
        self.score_2 = score_2
