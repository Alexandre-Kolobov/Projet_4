data_path = "data\\tournaments\\"
winer_point = 1
loser_point = 0
equality_point = 0,5


class Match:
    def __init__(self, name, player_1, player_2, score_1=0, score_2=0):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def __repr__(self):
        # return f"([{self.player_1},{self.score_1}], [{self.player_2},{self.score_2}])"
        return (f"Match: {self.player_1} vs {self.player_2} ---- Score {self.score_1}:{self.score_2}")

    def give_player_1(self):
        return self.player_1

    def give_player_2(self):
        return self.player_2

    def give_player_1_score(self):
        return self.score_1

    def give_player_2_score(self):
        return self.score_2

    def update_match_score(self, player_1_name, player_2_name, match_result):
        if match_result == player_1_name:
            self.score_1 = winer_point
            self.score_2 = loser_point
        elif match_result == player_2_name:
            self.score_1 = loser_point
            self.score_2 = winer_point
        else:
            self.score_1 = equality_point
            self.score_2 = equality_point

    def check_if_match_played(self):
        if self.score_1 == 0 and self.score_2 == 0:
            return False
        else:
            return True
