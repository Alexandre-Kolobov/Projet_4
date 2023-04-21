from views.view_tournament import View_tournament
from views.view_player import View_player
from views.view_match import View_match
from views.view_round import View_round
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from datetime import datetime
import random


class Controller_match:
    def __init__(self):
        # self.tournament = Tournament()
        self.view_tournament = View_tournament()
        self.view_player = View_player()
        self.view_match = View_match()
        self.view_round = View_round()

    def create_match(self, match_name, player_1, player_2):
        """Création de match"""
        match = Match(match_name, player_1, player_2)
        return match

    
    def play_match(self, player_1_name, player_2_name, match):
        """Joue le match"""
        # player_1 = match.give_player_1()
        # player_2 = match.give_player_2()

        # player_1_name = player_1.give_player_name()
        # player_2_name = player_2.give_player_name()

        match_result = self.view_match.play_match(player_1_name, player_2_name)
        match.update_match_score(player_1_name, player_2_name, match_result)

        player_1_score = match.give_player_1_score()
        player_2_score = match.give_player_2_score()

        self.view_match.show_match_result(player_1_name, player_2_name, player_1_score, player_2_score)


    def load_match(self, player_1, player_2, match):
        match_to_load = Match(name=match["name"],
                              player_1=player_1,
                              player_2=player_2,
                              score_1=match["score_1"],
                              score_2=match["score_2"])
        
        return match_to_load
            
    def players_names_to_check(self, match):
        player_1_to_load = (match["player_1"]["first_name"] + " " + match["player_1"]["family_name"])
        player_2_to_load = (match["player_2"]["first_name"] + " " + match["player_2"]["family_name"])

        return player_1_to_load, player_2_to_load

    def give_dict_players(self, match):
        player_1 = match.give_player_1()
        player_1_score = match.give_player_1_score()
        player_2 = match.give_player_2()
        player_2_score = match.give_player_2_score()
        players = {player_1:player_1_score, player_2:player_2_score}
        return players

    def check_if_match_played(self, match):
        return match.check_if_match_played()