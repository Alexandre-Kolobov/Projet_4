import json
import os

data_path = "data\\tournaments\\"

class Player:
    # def __init__ (self, first_name, family_name, birth_date, score = 0, random_number = 0, ingame = False):
    def __init__ (self, first_name, family_name, birth_date):
        self.first_name = first_name
        self.family_name = family_name
        self.birth_date = birth_date
        # self.score = score
        # self.random_number = random_number
        # self.ingame = ingame
        # self.played_with = []

    def __repr__(self):
        return(f"{self.first_name} {self.family_name}")

    # def add_random_number(self, random_number):
    #     self.random_number = random_number

    def give_player_name(self):
        return(f"{self.first_name} {self.family_name}")
    
    # def update_player_score(self, score):
    #     self.score += int(score)

    # def give_player_score(self):
    #     return self.score
    
    # def update_ingame_status(self, ingame):
    #     self.ingame = ingame

    # def give_ingame_status(self):
    #     return self.ingame

    # def add_played_with(self, player):
    #     self.played_with.append(player)

    # def check_played_with(self, player):
    #     if player in self.played_with:
    #         return True
    #     else:
    #         return False
        
    def save_players_json(self, tournament_name):
        json_dict = {
            "first_name":self.first_name,
            "family_name":self.family_name,
            "birth_date":self.birth_date
        }

        os.makedirs(data_path + tournament_name, exist_ok=True)

        with open(data_path + tournament_name + "\\players.json", "a") as json_file:
            json.dump(json_dict, json_file, indent=4)
        
class Player_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Player):
            return {
                "first_name": obj.first_name,
                "family_name":obj.family_name,
                    }
        return super().default(obj)