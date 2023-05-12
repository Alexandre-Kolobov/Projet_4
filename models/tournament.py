import json
import os
data_path = "data\\tournaments\\"


class Tournament():
    def __init__(self, name="",
                 place="",
                 date_start="",
                 date_finish="",
                 round_all=4,
                 round_current=0,
                 description="",
                 date_start_schedule="",
                 date_finish_schedule=""):

        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_finish = date_finish
        self.round_current = round_current
        self.round_list = []
        self.players_list = []
        self.description = description
        self.round_all = round_all
        self.date_start_schedule = date_start_schedule
        self.date_finish_schedule = date_finish_schedule

    def tournament_status(self):
        """Statut d'un tournoi"""
        tournament_dict = {"name": self.name,
                           "date_start": self.date_start,
                           "date_finish": self.date_finish,
                           "round_current": self.round_current,
                           "round_all": self.round_all,
                           "date_start_schedule": self.date_start_schedule,
                           "date_finish_schedule": self.date_finish_schedule,
                           }

        return tournament_dict

    def modify_start_information(self,
                                 name,
                                 place,
                                 date_start,
                                 description,
                                 round_all,
                                 date_start_schedule,
                                 date_finish_schedule):
        """Mise à jour des infos d'un tournoi"""
        self.name = name
        self.place = place
        self.date_start = date_start
        self.description = description
        self.round_all = int(round_all)
        self.date_start_schedule = date_start_schedule
        self.date_finish_schedule = date_finish_schedule

    def update_current_round(self):
        """Mise à jour du round en cours"""
        self.round_current = self.round_current + 1

    def update_start_date(self, date_start_real):
        self.date_start = date_start_real

    def give_current_round(self):
        """Return le round en cours"""
        return self.round_current

    def add_player(self, player):
        """Ajout un joueur au tournois"""
        self.players_list.append(player)

    def give_len_list_players(self):
        """Return le nombre des participants"""
        return len(self.players_list)

    def give_list_players(self):
        """Return la liste des participants"""
        return self.players_list

    def give_round_all_information(self):
        """Return le nombre des round à jouer"""
        return self.round_all

    def give_round_list(self):
        """Return la liste des rounds"""
        return self.round_list

    def add_round(self, round):
        """Ajout un round au torunoi"""
        self.round_list.append(round)

    def add_date_finish(self, date_finish):
        """Ajout la date de fin d'un tournoi"""
        self.date_finish = date_finish

    def save_tournament(self):
        # Si on dans l'objet qu'on serialize, on rencontre des objets imbriqués, method dumps ne sais pas le traiter.
        # Le parametre "default" nous permet de definir une fonction pour ces objets imbriqués.
        # o represente l'objet imbriqué
        # json_string = json.dumps(self.tournament, default=lambda o: o.__dict__, indent=4)
        if not os.path.exists(data_path):
            os.makedirs(data_path)

        file_name = (self.name + ".json")
        with open(data_path + file_name, "w") as json_file:
            json.dump(self.__dict__, json_file, default=lambda o: o.__dict__, indent=4)

    @staticmethod
    def give_number_min_players(round_all):
        """Donne le nombre minimum des joueurs pour faire un tournoi"""
        if (round_all % 2) == 0:
            min_players = round_all + 2
        else:
            min_players = round_all + 1

        return min_players

    @classmethod
    def give_database_tournaments(cls):
        """Return la liste des tournois enregistrés"""
        if not os.path.exists(data_path):
            os.makedirs(data_path)

        database_tournaments = []
        for filename in os.listdir(data_path):
            filename_without_extension = filename[:-5]

            json_dict = cls.load_tournament(filename_without_extension)
            tournament_name = json_dict["name"]
            database_tournaments.append(tournament_name)

        return database_tournaments

    @staticmethod
    def load_tournament(tournois):
        """Charge un tournois enregistré"""
        if not os.path.exists(data_path):
            os.makedirs(data_path)

        with open(data_path + tournois + ".json") as myfile:
            json_dict = json.load(myfile)

            return json_dict
