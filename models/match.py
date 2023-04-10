import json
import os
from models.player import Player_encoder

data_path = "data\\tournaments\\"

class Match: # match
    def __init__(self, name, player_1, player_2, score_1= 0, score_2 = 0):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def __repr__(self):
        return f"([{self.player_1},{self.score_1}], [{self.player_2},{self.score_2}])"
    
    # def __eq__(self, other):
    #     if isinstance(other, Match):
    #         if self.player_1 == other.player_2 and self.player_2 == other.player_1:
    #             return self.player_1 == other.player_2 and self.player_2 == other.player_1
    #         elif self.player_1 == other.player_1 and self.player_2 == other.player_2:
    #             return self.player_1 == other.player_1 and self.player_2 == other.player_2
    #         else:
    #             return False
    #     return False
    
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

    def save_matchs_json(self, tournament_name):
        json_dict = {
            "name":self.name,
            "player_1":self.player_1,
            "player_2":self.player_2,
            "score_1" :self.score_1,
            "score_2" :self.score_2
        }

        os.makedirs(data_path + tournament_name, exist_ok=True)

        with open(data_path + tournament_name + "\\matchs.json", "a") as json_file:
            json.dump(json_dict, json_file, indent=4, cls=Player_encoder)

