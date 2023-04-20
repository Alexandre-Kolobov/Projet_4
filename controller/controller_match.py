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

    # def create_matchs(self, tournament, round, players):
    #     round_name = round.give_round_name()
    #     # players = self.shuffle_players(round_name, tournament)
    #     self.create_pairs(players, round, tournament)
    #     matchs = round.give_match_list()
    #     self.view_round.show_round(matchs, round_name)
    #     tournament.save_tournament()
    #     return matchs
    
    # def create_pairs(self, players, round, tournament):
    #     """Création des paires"""
    #     players_tmp = players[:]  # players_tmp = players.copy() - même signification

    #     for player_1 in players:
    #         for player_2 in players:
    #             if player_1 in players_tmp and player_2 in players_tmp:
    #                 if player_1 != player_2 and not self.check_alredy_played(player_1, player_2, tournament):

    #                     try:
    #                         index_player_1 = players_tmp.index(player_1)
    #                         players_tmp.pop(index_player_1)

    #                     except ValueError:
    #                         pass

    #                     try:
    #                         index_player_2 = players_tmp.index(player_2)
    #                         players_tmp.pop(index_player_2)

    #                     except ValueError:
    #                         pass

    #                     self.create_match(round, player_1, player_2)

    #     if len(players_tmp) != 0:
    #         i = 0
    #         while i < len(players_tmp):
    #             self.create_match(round, players_tmp[i], players_tmp[i+1])
    #             i += 2

    # def create_match(self, round, player_1, player_2):
    #     """Création de match"""
    #     match_name = round.generate_match_name()
    #     match = Match(match_name, player_1, player_2)
    #     round.add_match(match)

    def create_match(self, match_name, player_1, player_2):
        """Création de match"""
        match = Match(match_name, player_1, player_2)
        return match
        

    # def check_alredy_played(self, player_1, player_2, tournament):
    #     """Verfication si les joueurs ont déja joué ensemble"""
    #     for round in tournament.give_round_list():
    #         for match in round.give_match_list():
    #             checked_player_1 = match.give_player_1()
    #             checked_player_2 = match.give_player_2()
    #             if player_1 == checked_player_1 or player_1 == checked_player_2:
    #                 if player_2 == checked_player_1 or player_2 == checked_player_2:
    #                     return True

    #     return False
    
    def play_match(self, match):
        """Joue le match"""
        player_1 = match.give_player_1()
        player_2 = match.give_player_2()

        player_1_name = player_1.give_player_name()
        player_2_name = player_2.give_player_name()

        match_result = self.view_match.play_match(player_1_name, player_2_name)
        match.update_match_score(player_1_name, player_2_name, match_result)

        player_1_score = match.give_player_1_score()
        player_2_score = match.give_player_2_score()

        self.view_match.show_match_result(player_1_name, player_2_name, player_1_score, player_2_score)


    def load_match(self, tournament, round, match):

        player_1_to_load = (match["player_1"]["first_name"] + " " + match["player_1"]["family_name"])
        player_2_to_load = (match["player_2"]["first_name"] + " " + match["player_2"]["family_name"])
        players = tournament.give_list_players()

        for player in players:
            player_name = player.give_player_name()
            
            if player_1_to_load == player_name:
                player_1_to_add = player
            
            if player_2_to_load == player_name:
                player_2_to_add = player
        
        match_to_load = Match(name=match["name"],
                              player_1=player_1_to_add,
                              player_2=player_2_to_add,
                              score_1=match["score_1"],
                              score_2=match["score_2"])
        

        round.add_match(match_to_load)
        tournament.save_tournament()

    def give_dict_players(self, match):
        player_1 = match.give_player_1()
        player_1_score = match.give_player_1_score()
        player_2 = match.give_player_2()
        player_2_score = match.give_player_2_score()
        players = {player_1:player_1_score, player_2:player_2_score}
        return players
