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
    
    def save_player(self):
        # Si on dans l'objet qu'on serialize, on rencontre des objets imbriqués, method dumps ne sais pas le traiter.
        # Le parametre "default" nous permet de definir une fonction pour ces objets imbriqués. 
        # o represente l'objet imbriqué
        # json_string = json.dumps(self.tournament, default=lambda o: o.__dict__, indent=4)

        file_name = (self.first_name + " " + self.family_name)
        with open (data_path + file_name, "w") as json_file:
            json.dump(self.__dict__, json_file, indent=4)

    @staticmethod
    def give_database_players():
        database_players = []
        for filename in os.listdir(data_path):
            database_players.append(filename)
        
        return(database_players)
    
    @staticmethod
    def load_player(player):
        with open (data_path + player) as myfile:
            json_dict = json.load(myfile)
            return json_dict
        
    @staticmethod
    def load_player_from_dict(player):
            json_dict = json.loads(player)
            return json_dict
