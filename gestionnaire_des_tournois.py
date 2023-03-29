# import json
from models.tournament import Tournament
from controller.controller import Controller
from models.player import Player
from views.views import View


def main():
   
    play_tournament = Controller()
    # play_tournament.creat_tournament()
    # play_tournament.get_players()
    max_round = play_tournament.round_estimation()
    play_tournament.round_proposition(5)
    play_tournament.create_rounds()





    # player_1 = Player(first_name = "aa", family_name ="aa", birth_date = "05101992", score = 4)
    # player_2 = Player(first_name = "bb", family_name ="bb", birth_date = "05101992", score = 3)
    # player_3 = Player(first_name = "cc", family_name ="cc", birth_date = "05101992", score = 4)
    # player_4 = Player(first_name = "dd", family_name ="dd", birth_date = "05101992", score = 2)
    # player_5 = Player(first_name = "ee", family_name ="ee", birth_date = "05101992", score = 1)

    # players = [player_1, player_2, player_3, player_4, player_5]

    # tournament.generate_pairs(players)
    
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
