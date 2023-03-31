class Match: # match
    def __init__(self, name, player_1, player_2, score_1= 0, score_2 = 0):
        # self.game = ([player_1, score_1], [player_2, score_2])
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2
        # gerer les joueurs qui se sont déja rencotré

    def __repr__(self):
        return f"{self.player_1}:{self.score_1} vs {self.player_2}:{self.score_2}"
    
    def __eq__(self, other):
        if isinstance(other, Match):
            if self.player_1 == other.player_2 and self.player_2 == other.player_1:
                print (f"Cas 1: {self.player_1} : {self.player_2} et {other.player_1} : {other.player_2}" )
                return self.player_1 == other.player_2 and self.player_2 == other.player_1
            elif self.player_1 == other.player_1 and self.player_2 == other.player_2:
                print (f"Cas 2: {self.player_1} : {self.player_2} et {other.player_1} : {other.player_2}")
                return self.player_1 == other.player_1 and self.player_2 == other.player_2
            else:
                print (f"Cas 3: {self.player_1} : {self.player_2} et {other.player_1} : {other.player_2}")
                return False
        return False