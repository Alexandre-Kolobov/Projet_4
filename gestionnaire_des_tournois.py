import json
from models.player import Player
from views.views import View

class Club:
    def __init__ (self, id):
        self.id = id # l'identifiant national d’échecs


class Tournament:
    def __init__(self, name, place, date_start, date_finish, round_current, round_list, players_list, description, round_all = "4"):
        pass

    def round_estimation(self):
        pass

class Round(Tournament):
    def __init__(self, name, date_start, date_finish):
        pass

class Game(Round):
    def __init__(self, player_1, player_2):
        pass

    def get_points(self):
        pass


class Controller:
    def __init__(self):
        self.players = []
    

    def get_players(self):
        
        player_informations = View().get_player_informations()

        first_name = player_informations[0]
        family_name = player_informations[1]
        birth_date = player_informations[2]
        add_player = player_informations[3]

        player = Player(first_name, family_name, birth_date)
        self.players.append(player)

        if add_player == "y":
            self.get_players()
            
        return self.players


def main():
    test = Controller()
    test.get_players()

    print("Voici la liste des joueurs participants:")

    for i in test.players:
        print (i)

main()
