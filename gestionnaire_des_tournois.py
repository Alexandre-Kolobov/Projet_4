# import json
from models.tournament import Tournament, Round
from controller.controller import Controller
from models.player import Player


class Club:
    def __init__(self, id):
        self.id = id  # l'identifiant national d’échecs

def main():
    # test = Controller()
    # test.create_pairs()
    # test.play_game()

    tournament_instance = Tournament(name = "T1", place = "Paris", date_start = "14082023")

    tournament = Controller()

    player_1 = Player(first_name = "aa", family_name ="aa", birth_date = "05101992", score = 4)
    player_2 = Player(first_name = "bb", family_name ="bb", birth_date = "05101992", score = 3)
    player_3 = Player(first_name = "cc", family_name ="cc", birth_date = "05101992", score = 4)
    player_4 = Player(first_name = "dd", family_name ="dd", birth_date = "05101992", score = 2)

    players = [player_1, player_2, player_3, player_4]

    tournament.generate_pairs (players)
    
    # round_estimation = tournament.round_estimation()
    # # round_estimation = 3
    # round_proposition = tournament.round_proposition(round_estimation)
    # list_rounds = tournament.generate_list_round(round_estimation)
    # tournament_instance.round_all = round_proposition
    # tournament_instance.players_list = tournament.players

    # list_rounds = tournament.generate_list_round(3)
    # tournament_instance.round_list = list_rounds

    # date_finish = tournament.play_rounds(list_rounds)
    # tournament_instance.date_finish = date_finish




main()
