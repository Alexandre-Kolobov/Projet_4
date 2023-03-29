class Match: # match
    def __init__(self, player_1, score_1, player_2, score_2):
        # self.game = ([player_1, score_1], [player_2, score_2])
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2
        # gerer les joueurs qui se sont déja rencotré

    def __repr__(self):
        return f"{self.player_1}:{self.score_1} vs {self.player_2}:{self.score_2}"