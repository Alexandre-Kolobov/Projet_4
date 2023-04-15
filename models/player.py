import json
import os
data_path = "data\\players\\"


class Player():
    def __init__(self, first_name, family_name, birth_date):
        self.first_name = first_name
        self.family_name = family_name
        self.birth_date = birth_date

    def __repr__(self):
        return (f"{self.first_name} {self.family_name}")

    def give_player_name(self):
        return (f"{self.first_name} {self.family_name}")
    
    def save_player(self, player_name):
        # Si on dans l'objet qu'on serialize, on rencontre des objets imbriqués, method dumps ne sais pas le traiter.
        # Le parametre "default" nous permet de definir une fonction pour ces objets imbriqués. 
        # o represente l'objet imbriqué
        # json_string = json.dumps(self.tournament, default=lambda o: o.__dict__, indent=4)

        with open (data_path + player_name, "a") as json_file:
            json.dump(self.__dict__, json_file, indent=4)

    @classmethod
    def give_database_players(csl):
        database_players = []
        for filename in os.listdir(data_path):
            database_players.append(filename)
        
        return(database_players)
    
    @classmethod
    def load_player(csl, player):    
        with open (data_path + player) as myfile:
            json_dict = json.load(myfile)
            return Player(json_dict["first_name"], json_dict["family_name"], json_dict["birth_date"])
