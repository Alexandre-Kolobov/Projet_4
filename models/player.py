import json
import os
data_path = "data\\players\\"
counter_path = "data\\counter\\"
counter_filename = "id_counter.txt"


class Player():
    counter = 0

    def __init__(self, first_name, family_name, birth_date, counter):
        self.first_name = first_name
        self.family_name = family_name
        self.birth_date = birth_date
        self.counter = counter

    def __repr__(self):
        return (f"{self.first_name} {self.family_name} p{self.counter}")

    def give_player_name(self):
        """Renvoi le nom d'un joueur"""
        return (f"{self.first_name} {self.family_name} p{self.counter}")

    def save_player(self):
        """Sauvegarde d'un player sous format json"""
        # Si on dans l'objet qu'on serialize, on rencontre des objets imbriqués, method dumps ne sais pas le traiter.
        # Le parametre "default" nous permet de definir une fonction pour ces objets imbriqués.
        # o represente l'objet imbriqué
        # json_string = json.dumps(self.tournament, default=lambda o: o.__dict__, indent=4)
        if not os.path.exists(data_path):
            os.mkdir(data_path)

        file_name = (self.first_name + " " + self.family_name + " " + "p" + str(self.counter))
        with open(data_path + file_name, "w") as json_file:
            json.dump(self.__dict__, json_file, indent=4)

    @staticmethod
    def give_database_players():
        """Return une list des joueurs existants"""
        if not os.path.exists(data_path):
            os.mkdir(data_path)

        database_players = []
        for filename in os.listdir(data_path):
            database_players.append(filename)

        return database_players

    @staticmethod
    def load_player(id):
        """Charge un joueur"""
        if not os.path.exists(data_path):
            os.mkdir(data_path)

        for file_name in os.listdir(data_path):
            if id in file_name:
                with open(data_path + file_name) as myfile:
                    json_dict = json.load(myfile)
                    return json_dict

    @classmethod
    def increment_counter(cls):
        cls.counter = cls.counter + 1
        filename = (counter_path + counter_filename)
        with open(filename, "w") as myfile:
            myfile.write(str(cls.counter))

    @classmethod
    def load_counter(cls):
        filename = (counter_path + counter_filename)
        if os.path.exists(filename):
            with open(filename, "r") as myfile:
                cls.counter = int(myfile.read())
        else:
            os.mkdir(counter_path)
            filename = (counter_path + counter_filename)
            with open(filename, "w") as myfile:
                myfile.write(str(cls.counter))
        return cls.counter
