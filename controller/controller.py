from views.view_tournament import View_tournament
from views.view_player import View_player
from views.view_match import View_match
from views.view_round import View_round
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from datetime import datetime
import random
import json

class Controller_player:
    def __init__(self):
        self.tournament = Tournament()
        self.view_tournament = View_tournament()
        self.view_player = View_player()
    
    def give_players_in_tournament(self):
        """Affiche la liste des joueurs en temps réel"""
        players_in_turnament = self.tournament.give_list_players()
        player_name_in_turnament = []
        for player in players_in_turnament:
            name = player.give_player_name()
            player_name_in_turnament.append(name)
        
        return player_name_in_turnament

    def get_players(self):
        """Création des participants"""
        while True:
            player_name_in_turnament = self.give_players_in_tournament()
            if len(player_name_in_turnament) != 0:
                self.view_player.show_players(player_name_in_turnament)

            database_players = Player.give_database_players()
            answer = self.view_player.show_menu_player(database_players)

            """TEST"""
            player_1 = Player("a", "a", "05101992")
            self.tournament.add_player(player_1)


            if answer == "Selectionner":
                player_name_in_turnament = self.give_players_in_tournament()
                selected_player = self.view_player.select_player_from_database(database_players, 
                                                                               player_name_in_turnament)

                if selected_player != None:
                    loaded_player = Player.load_player(selected_player)
                    self.tournament.add_player(loaded_player)

            if answer == "Ajouter":
                player_informations = self.view_player.get_player_informations(database_players)

                if player_informations != None:
                    first_name = player_informations[0]
                    family_name = player_informations[1]
                    birth_date = player_informations[2]

                    player_to_save = Player(first_name, family_name, birth_date)
                    player_to_save.save_player()

        # self.get_players_test()

    # def get_players_test(self):
    #     player_1 = Player("a", "a", "05101992")
    #     self.tournament.add_player(player_1)
    #     player_1.save_player()


    #     player_2 = Player("b", "b", "05101992")
    #     self.tournament.add_player(player_2)
    #     player_2.save_player()

    #     player_3 = Player("c", "c", "05101992")
    #     self.tournament.add_player(player_3)
    #     player_4 = Player("d", "d", "05101992")
    #     self.tournament.add_player(player_4)
    #     player_5 = Player("e", "e", "05101992")
    #     self.tournament.add_player(player_5)
    #     player_6 = Player("f", "f", "05101992")
    #     self.tournament.add_player(player_6)
        # player_7 = Player("g", "g", "05101992")
        # self.tournament.add_player(player_7)
        # player_8 = Player("h", "h", "05101992")
        # self.tournament.add_player(player_8)
        # self.save_tournament_json()

    def check_number_players(self):
        """Verifie la possibilité de jouer le nombre des rounds demandé"""
        participants_len = self.tournament.give_len_list_players()
        round_all = self.tournament.give_round_all_information()

        if (participants_len % 2) == 0:  # Si nombre des participant est paire il y a N-1 tours possibles
            max_round = participants_len - 1
            if max_round >= round_all:
                self.view_round.show_round_estimation(round_all)
            else:
                self.view_round.show_round_negative_estimation(round_all)
                self.get_players()
        else:  # Si nombre des participant est impaire, il faut ajouter des joueurs
            self.view_round.show_round_negative_estimation(round_all)
            self.get_players()

        participants = self.tournament.give_list_players()
        self.view_player.show_players(participants)

class Controller_game:
    def __init__(self):
        self.tournament = Tournament()
        self.view_tournament = View_tournament()
        self.view_player = View_player()
        self.view_match = View_match()
        self.view_round = View_round()

    def creat_tournament(self):
        """Initialise un tournois"""
        round_all = self.tournament.give_round_all_information()
        tournament_informations = self.view_tournament.get_tournament_start_informations(round_all)
        name = tournament_informations[0]
        place = tournament_informations[1]

        round_all_update = tournament_informations[3]
        date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.tournament.modify_start_information(name, place, date_start, round_all_update)

    def create_list_rounds(self):
        """Création des rounds vides"""
        rounds = self.tournament.give_round_all_information()
        i = 1

        while i <= rounds:
            round_name = self.tournament.generate_round_name(i)
            round = Round(name=round_name)
            self.tournament.add_round(round)
            i += 1

    def play_rounds(self):
        """Joue les rounds"""
        rounds = self.tournament.give_round_list()
        for round in rounds:
            if not round.give_finish_status():
                round.start_round()
                round_name = round.give_round_name()
                players = self.shuffle_players(round_name)
                matchs = round.give_match_list()

                if len(matchs) == 0:
                    # Si les matchs ne sont pas créer dans un round, on le créer et les joue
                    self.create_pairs(players, round)
                    self.view_round.show_round(matchs, round_name)
                    matchs = round.give_match_list()
                    for match in matchs:
                        self.play_match(match)
                else:
                    for match in matchs:
                        match_score_player_1 = match.give_player_1_score()
                        match_score_player_2 = match.give_player_2_score()
                        if match_score_player_1 == 0 and match_score_player_2 == 0:
                            # S'il y a des matchs non joués dans un round on les joue
                            self.play_match(match)
                        else:
                            # On affiche le match s'il a déja été joué
                            player_1 = match.give_player_1()
                            player_2 = match.give_player_2()
                            player_1_name = player_1.give_player_name()
                            player_2_name = player_2.give_player_name()

                            player_1_score = match.give_player_1_score()
                            player_2_score = match.give_player_2_score()

                            self.view_match.played_match(player_1_name, player_2_name, player_1_score, player_2_score)

            for player in players:
                score = self.give_player_score(player)
                self.view_player.show_player_score(player, score)

            finish_status = self.view_round.get_finish_round(round_name)
            round.update_finish_status(finish_status)

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

    def shuffle_players(self, round_name):
        """Melange les joueurs"""
        players = self.tournament.give_list_players()

        if round_name == "Round_1":
            random.shuffle(players)
        else:
            players.sort(key=lambda p: self.give_player_score(p), reverse=True)  # p reprensent objet Player
        return players

    def create_pairs(self, players, round):
        """Création des paires"""
        players_tmp = players[:]  # players_tmp = players.copy() - même signification

        for player_1 in players:
            for player_2 in players:
                if player_1 in players_tmp and player_2 in players_tmp:
                    if player_1 != player_2 and not self.check_alredy_played(player_1, player_2):

                        try:
                            index_player_1 = players_tmp.index(player_1)
                            players_tmp.pop(index_player_1)

                        except ValueError:
                            pass

                        try:
                            index_player_2 = players_tmp.index(player_2)
                            players_tmp.pop(index_player_2)

                        except ValueError:
                            pass

                        self.create_match(round, player_1, player_2)

        if len(players_tmp) != 0:
            i = 0
            while i < len(players_tmp):
                self.create_match(round, players_tmp[i], players_tmp[i+1])
                i += 2

    def create_match(self, round, player_1, player_2):
        """Création de match"""
        match_name = round.generate_match_name()
        match = Match(match_name, player_1, player_2)
        round.add_match(match)

    def check_alredy_played(self, player_1, player_2):
        """Verfication si les joueurs ont déja joué ensemble"""
        for round in self.tournament.give_round_list():
            for match in round.give_match_list():
                checked_player_1 = match.give_player_1()
                checked_player_2 = match.give_player_2()
                if player_1 == checked_player_1 or player_1 == checked_player_2:
                    if player_2 == checked_player_1 or player_2 == checked_player_2:
                        return True

        return False

    def give_player_score(self, player):
        """Donne le score d'un joueur"""
        player_score = 0
        for round in self.tournament.give_round_list():
            for match in round.give_match_list():
                checked_player_1 = match.give_player_1()
                checked_player_2 = match.give_player_2()

                if player == checked_player_1:
                    player_score = int(player_score) + int(match.give_player_1_score())
                elif player == checked_player_2:
                    player_score = int(player_score) + int(match.give_player_2_score())

        return player_score

    def classement(self):
        """Classment des joueurs par leur score - du plus élevé au plus petit"""
        players = self.tournament.give_list_players()
        players.sort(key=lambda p: self.give_player_score(p), reverse=True)

        place = 1
        for player in players:
            score = self.give_player_score(player)
            self.view_tournament.show_classment(player, place, score)
            place += 1
