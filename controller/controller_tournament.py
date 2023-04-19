from views.view_tournament import View_tournament
from views.view_player import View_player
from views.view_match import View_match
from views.view_round import View_round
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from datetime import datetime
import random


class Controller_tournament:
    def __init__(self):
        # self.tournament = Tournament()
        self.view_tournament = View_tournament()
        self.view_player = View_player()
        self.view_match = View_match()
        self.view_round = View_round()

    def create_tournament(self):
        """Initialise un tournois"""
        while True:
            database_tournois = Tournament.give_database_tournaments()
            answer = self.view_tournament.show_menu_tournament(database_tournois)
            
            if answer == "Selectionner":
                tournament_informations = self.load_tournament(database_tournois)
                return tournament_informations

            if answer == "Creer":
                tournament_informations = self.new_tournament(database_tournois)
                return tournament_informations
            
    def load_tournament(self, database_tournois):
        selected_tournament = self.view_tournament.select_tournament_from_database(database_tournois)

        if selected_tournament != None:
            selected_to_load_tournament = Tournament.load_tournament(selected_tournament)
            tournament = Tournament(name=selected_to_load_tournament["name"],
                                    place=selected_to_load_tournament["place"],
                                    date_start=selected_to_load_tournament["date_start"],
                                    date_finish=selected_to_load_tournament["date_finish"],
                                    round_all=selected_to_load_tournament["round_all"],
                                    round_current=selected_to_load_tournament["round_current"],
                                    description=selected_to_load_tournament["description"])
            
            players_list = selected_to_load_tournament["players_list"]
            round_list = selected_to_load_tournament["round_list"]
            current_round = selected_to_load_tournament["round_current"]
            return tournament, players_list, round_list, current_round
        
    def new_tournament(self, database_tournois):
        tournament = Tournament()
        round_all = tournament.give_round_all_information()
        tournament_informations = self.view_tournament.get_tournament_start_informations(round_all, database_tournois)
        name = tournament_informations[0]
        place = tournament_informations[1]
        round_all_update = tournament_informations[3]
        date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        tournament.modify_start_information(name, place, date_start, round_all_update)
        tournament.save_tournament()

        round_all = tournament.give_round_all_information()

        players_list = []
        round_list = []
        current_round = tournament.give_current_round()

        return tournament, players_list, round_list, current_round




    # def play_rounds(self, tournament):
    #     """Joue les rounds"""
    #     rounds = tournament.give_round_list()
    #     for round in rounds:
    #         if not round.give_finish_status():
    #             round.start_round()
    #             round_name = round.give_round_name()
    #             players = self.shuffle_players(round_name, tournament)
    #             matchs = round.give_match_list()

    #             if len(matchs) == 0:
    #                 # Si les matchs ne sont pas créer dans un round, on le créer et les joue
    #                 self.create_pairs(players, round, tournament)
    #                 self.view_round.show_round(matchs, round_name)
    #                 matchs = round.give_match_list()
    #                 for match in matchs:
    #                     self.play_match(match)
    #                     tournament.save_tournament()
    #             else:
    #                 for match in matchs:
    #                     match_score_player_1 = match.give_player_1_score()
    #                     match_score_player_2 = match.give_player_2_score()
    #                     if match_score_player_1 == 0 and match_score_player_2 == 0:
    #                         # S'il y a des matchs non joués dans un round on les joue
    #                         self.play_match(match)
    #                     else:
    #                         # On affiche le match s'il a déja été joué
    #                         player_1 = match.give_player_1()
    #                         player_2 = match.give_player_2()
    #                         player_1_name = player_1.give_player_name()
    #                         player_2_name = player_2.give_player_name()

    #                         player_1_score = match.give_player_1_score()
    #                         player_2_score = match.give_player_2_score()

    #                         self.view_match.played_match(player_1_name, player_2_name, player_1_score, player_2_score)

    #         for player in players:
    #             score = self.give_player_score(player, tournament)
    #             self.view_player.show_player_score(player, score)

    #         finish_status = self.view_round.get_finish_round(round_name)
    #         round.update_finish_status(finish_status)

    # def play_match(self, tournament, match):
    #     """Joue le match"""
    #     player_1 = match.give_player_1()
    #     player_2 = match.give_player_2()

    #     player_1_name = player_1.give_player_name()
    #     player_2_name = player_2.give_player_name()

    #     match_result = self.view_match.play_match(player_1_name, player_2_name)
    #     match.update_match_score(player_1_name, player_2_name, match_result)

    #     player_1_score = match.give_player_1_score()
    #     player_2_score = match.give_player_2_score()

    #     self.view_match.show_match_result(player_1_name, player_2_name, player_1_score, player_2_score)
    #     tournament.save_tournament()

    # def shuffle_players(self, round_name, tournament):
    #     """Melange les joueurs"""
    #     players = tournament.give_list_players()

    #     if round_name == "Round_1":
    #         random.shuffle(players)
    #     else:
    #         players.sort(key=lambda p: self.give_player_score(p, tournament), reverse=True)  # p reprensent objet Player
    #     return players

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

    # def give_player_score(self, player, tournament):
    #     """Donne le score d'un joueur"""
    #     player_score = 0
    #     for round in tournament.give_round_list():
    #         for match in round.give_match_list():
    #             checked_player_1 = match.give_player_1()
    #             checked_player_2 = match.give_player_2()

    #             if player == checked_player_1:
    #                 player_score = int(player_score) + int(match.give_player_1_score())
    #             elif player == checked_player_2:
    #                 player_score = int(player_score) + int(match.give_player_2_score())

    #     return player_score

    def classement(self, tournament):
        """Classment des joueurs par leur score - du plus élevé au plus petit"""
        players = tournament.give_list_players()
        players.sort(key=lambda p: self.give_player_score(p, tournament), reverse=True)

        place = 1
        for player in players:
            score = self.give_player_score(player, tournament)
            self.view_tournament.show_classment(player, place, score)
            place += 1

    def give_player_score(self, player, tournament):
        """Donne le score d'un joueur"""
        player_score = 0
        for round in tournament.give_round_list():
            for match in round.give_match_list():
                checked_player_1 = match.give_player_1()
                checked_player_2 = match.give_player_2()

                if player == checked_player_1:
                    player_score = int(player_score) + int(match.give_player_1_score())
                elif player == checked_player_2:
                    player_score = int(player_score) + int(match.give_player_2_score())

        return player_score

    def shuffle_players(self, tournament):
        """Melange les joueurs"""
        players = tournament.give_list_players()
        round = tournament.give_current_round()

        if round == 1:
            random.shuffle(players)
        else:
            players.sort(key=lambda p: self.give_player_score(p, tournament), reverse=True)  # p reprensent objet Player
        return players