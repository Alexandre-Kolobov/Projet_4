from views.view_tournament import View_tournament
from views.view_player import View_player
from views.view_match import View_match
from views.view_round import View_round
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from datetime import datetime
import random


class Controller_round:
    def __init__(self):
        # self.tournament = Tournament()
        self.view_tournament = View_tournament()
        self.view_player = View_player()
        self.view_match = View_match()
        self.view_round = View_round()

    def create_list_rounds(self, tournament):
        """Création des rounds vides"""
        rounds_all = tournament.give_round_all_information()
        i = 1

        while i <= rounds_all:
            round_name = tournament.generate_round_name(i)
            round = Round(name=round_name)
            tournament.add_round(round)
            i += 1

        tournament.save_tournament()
        rounds = tournament.give_round_list()
        return rounds
    
    def load_round(self, tournament, round):
        round_to_load = Round(name=round["name"],
                              date_start=round["date_start"],
                              date_finish=round["date_finish"],
                              finish_status=round["finish_status"])
        
        matchs = round["matchs"]

        tournament.add_round(round_to_load)
        tournament.save_tournament()

        return round_to_load, matchs
    
    # def load_rounds(self, tournament, round_list):
    #     if len(round_list) != 0:
    #         for round in round_list:
    #             round_to_load = Round(name=round["name"],
    #                                   date_start=round["date_start"],
    #                                   date_finish=round["date_finish"],finish_status=round["finish_status"])

    #             matchs = round["matchs"]

    #         #     for match in matchs:
    #         #         match_to_load = Match(name=match["name"],
    #         #                               player_1=match["player_1"],
    #         #                               player_2=match["player_2"],
    #         #                               score_1=match["score_1"],
    #         #                               score_2=match["score_2"])
                    
    #         #         round_to_load.add_match(match_to_load)


    #         #     tournament.add_round(round_to_load)
    #         # tournament.save_tournament()
    #         # rounds = tournament.give_round_list()
    #         return rounds
    
    def finish_round(self, tournament, round):
        round_name = round.give_round_name()
        finish_status = self.view_round.get_finish_round(round_name)
        round.update_finish_status(finish_status)
        tournament.save_tournament()