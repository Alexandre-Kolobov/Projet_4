import json
import os

data_path = "data\\tournaments\\"

class Player:
    def __init__ (self, first_name, family_name, birth_date):
        self.first_name = first_name
        self.family_name = family_name
        self.birth_date = birth_date

    def __repr__(self):
        return(f"{self.first_name} {self.family_name}")

    def give_player_name(self):
        return(f"{self.first_name} {self.family_name}")
        
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