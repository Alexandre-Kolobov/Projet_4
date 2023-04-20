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

    def create_round(self, round_name):
        """Création des rounds vides"""
        round = Round(name=round_name)
        return round
    
    def load_round(self, tournament, round):
        round_to_load = Round(name=round["name"],
                              date_start=round["date_start"],
                              date_finish=round["date_finish"],
                              finish_status=round["finish_status"])
        
        matchs = round["matchs"]

        tournament.add_round(round_to_load)
        tournament.save_tournament()

        return round_to_load, matchs

    def finish_round(self, round):
        round_name = round.give_round_name()
        finish_status = self.view_round.get_finish_round(round_name)
        round.update_finish_status(finish_status)

    def generate_match_name(self):
        match_counter += 1
        name = "Match_" + str(match_counter)
        return name
    
    def give_list_matchs(self, round):
        matchs_list = round.give_match_list()
        return matchs_list
    
    def add_match(self, round, match):
        round.add_match(match)