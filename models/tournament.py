import json
import os
data_path = "data\\tournaments\\"

class Tournament():
    def __init__(self, name="", place="", date_start="", date_finish="", round_all=4, round_current="", description=""):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_finish = date_finish
        self.round_current = round_current
        self.round_list = []
        self.players_list = []
        self.description = description
        self.round_all = round_all

    def modify_start_information(self, name, place, date_start, round_all):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.round_all = int(round_all)

    def add_player(self, player):
        self.players_list.append(player)

    def give_len_list_players(self):
        return len(self.players_list)

    def give_list_players(self):
        return self.players_list

    def give_round_all_information(self):
        return self.round_all

    def give_round_list(self):
        return self.round_list

    def add_round(self, round):
        self.round_list.append(round)

    def add_date_finish(self, date_finish):
        self.date_finish = date_finish

    def give_tournament_name(self):
        return self.name

    def generate_round_name(self, round):
        name = "Round_" + str(round)
        return name
    
    def save_tournament(self):
        # Si on dans l'objet qu'on serialize, on rencontre des objets imbriqués, method dumps ne sais pas le traiter.
        # Le parametre "default" nous permet de definir une fonction pour ces objets imbriqués. 
        # o represente l'objet imbriqué
        # json_string = json.dumps(self.tournament, default=lambda o: o.__dict__, indent=4)
        file_name = (self.name)
        with open (data_path + file_name, "w") as json_file:
            # json.dump(self.__dict__, json_file, indent=4)
            json.dump(self.__dict__, json_file, default=lambda o: o.__dict__, indent=4)

    @classmethod
    def give_database_tournaments(csl):
        database_tournaments = []
        for filename in os.listdir(data_path):
            database_tournaments.append(filename)
        
        return(database_tournaments)
    
    @classmethod
    def load_tournament(cls, tournois):    
        with open (data_path + tournois) as myfile:
            json_dict = json.load(myfile)
            loaded_tournament = Tournament(name=json_dict["name"],
                                           place=json_dict["place"],
                                           date_start=json_dict["date_start"],
                                           date_finish=json_dict["date_finish"],
                                           round_all=json_dict["round_all"],
                                           round_current=json_dict["round_current"],
                                           description=json_dict["description"])
            
            players_list = json_dict["players_list"]
            round_list = json_dict["round_list"]

            return loaded_tournament, players_list, round_list

        # self.name = json_dict["name"]
        # self.place = json_dict["place"]
        # self.date_start = json_dict["date_start"]
        # self.date_finish = json_dict["date_finish"]
        # self.round_current = json_dict["round_current"]
        # self.round_list = json_dict["round_list"]
        # self.players_list = json_dict["players_list"]
        # self.description = json_dict["description"]
        # self.round_all = json_dict["round_all"]
