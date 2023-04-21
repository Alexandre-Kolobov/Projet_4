from views.view_tournament import View_tournament
from views.view_player import View_player
from views.view_match import View_match
from views.view_round import View_round
from models.tournament import Tournament
from datetime import datetime
import random


class Controller_tournament:
    def __init__(self, player_controller, round_controller, match_controller):
        # self.tournament = Tournament()
        self.view_tournament = View_tournament()
        self.view_player = View_player()
        self.view_match = View_match()
        self.view_round = View_round()
        self.player_controller = player_controller
        self.round_controller = round_controller
        self.match_controller = match_controller

    def run(self):
        tournament_informations = self.create_tournament()
        tournament = tournament_informations[0]
        players_list = tournament_informations[1]
        round_list = tournament_informations[2]
        current_round = tournament_informations[3]

        # On charge les joueurs s'ils existent dans le tournois
        if len(players_list) != 0:
            for player in players_list:
                player_to_add = self.player_controller.load_players_from_tournament(player)
                tournament.add_player(player_to_add)
                tournament.save_tournament()

        #  Si les rounds n'ont pas été commencé (on continue la création des joueurs)
        if current_round == 0:
            while True:
                players_in_turnament = tournament.give_list_players()
                answer = self.player_controller.get_player(players_in_turnament)

                # if answer == "Afficher":
                #     pass

                if answer == "Ajouter":
                    player = self.player_controller.select_player(players_in_turnament)
                    tournament.add_player(player)
                    tournament.save_tournament()

                    
                    while True:
                        answer_one_more = self.player_controller.add_one_more_player()
                        if answer_one_more == "Oui":
                            player = self.player_controller.select_player(players_in_turnament)
                            tournament.add_player(player)
                            tournament.save_tournament()
                        else:
                            break
                
                if answer == "Creer":
                    self.player_controller.add_new_player()


                if answer == "Demmarer":
                    participants_len = tournament.give_len_list_players()
                    round_all = tournament.give_round_all_information()
                    if self.player_controller.check_number_players(participants_len, round_all):
                        break

                if answer == "Sauvegarder":
                    exit(0)
                
                if answer == "Revenir":
                    return True

            round_all = tournament.give_round_all_information()

            r = 1
            while r <= round_all:
                round_name = "Round_" + str(r)
                round = self.round_controller.create_round(round_name)
                r += 1
                tournament.add_round(round)
                tournament.save_tournament()

            rounds = tournament.give_round_list()
            for round in rounds:
                tournament.update_current_round()
                tournament.save_tournament()
                players = tournament.give_list_players()
                current_round = tournament.give_current_round()

                rounds_to_check = tournament.give_round_list()
                played_matchs = []
                for round_to_check in rounds_to_check:

                    matchs_list = self.round_controller.give_list_matchs(round_to_check)
                    for match_in_list in matchs_list:
                        played_matchs.append(match_in_list)
                    
                    played_pairs = []
                    for played_match in played_matchs:
                        players_dict = self.match_controller.give_dict_players(played_match)
                        played_pairs.append(players_dict)
                
                players = self.shuffle_players(players, current_round, played_pairs)

                played_pairs_list = list(played_pairs)  # played_pairs est un dictionnaire contenant tous matchs(jouers/score)
                pairs = self.create_pairs(players, played_pairs_list)

                m = 1
                for pair in pairs:
                    match_name = "Match_" + str(m)
                    m += 1
                
                    match = self.match_controller.create_match(match_name, pair[0], pair[1])
                    self.round_controller.add_match(round, match)
                    tournament.save_tournament()
 
                matchs_list_to_play = self.round_controller.give_list_matchs(round)
                for match_to_play in matchs_list_to_play:
                    players_match_dict = self.match_controller.give_dict_players(match_to_play)
                    players = list(players_match_dict)

                    player_1_name = self.player_controller.give_player_name(players[0])
                    player_2_name = self.player_controller.give_player_name(players[1])

                    self.match_controller.play_match(player_1_name, player_2_name, match_to_play)
                    tournament.save_tournament()

                self.round_controller.finish_round(round)
                tournament.save_tournament()
            
            date_finish = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            tournament.add_date_finish(date_finish)
            tournament.save_tournament()
            self.classement(tournament, played_pairs)

        else:

            for round in round_list:
                round_informations = self.round_controller.load_round(round)
                round_to_load = round_informations[0]
                matchs = round_informations[1]
                tournament.add_round(round_to_load)
                tournament.save_tournament()

                for match in matchs:
                    players = tournament.give_list_players()
                    players_names = self.match_controller.players_names_to_check(match) 
                    player_1_name = players_names[0]
                    player_2_name = players_names[1]

                    for player in players:
                        if self.player_controller.player_name_to_check(player_1_name, player) != None:
                            player_1 = self.player_controller.player_name_to_check(player_1_name, player)
                        
                        if self.player_controller.player_name_to_check(player_2_name, player) != None:
                            player_2 = self.player_controller.player_name_to_check(player_2_name, player)
    
                    loaded_match = self.match_controller.load_match(player_1, player_2, match)
                    self.round_controller.add_match(round_to_load, loaded_match)
                    tournament.save_tournament()
            
                if self.round_controller.check_finish_status(round_to_load) == False:
                    matchs_list_to_play = self.round_controller.give_list_matchs(round_to_load)
                    # Continuer tournament à partir d'un round (les matchs sont crées mais pas joués compeltement)
                    if len(matchs_list_to_play) != 0:
                        matchs_list_to_play = self.round_controller.give_list_matchs(round_to_load)
                        for match_to_play in matchs_list_to_play:
                            
                            if self.match_controller.check_if_match_played(match_to_play) == False:
                                players_match_dict = self.match_controller.give_dict_players(match_to_play)
                                players = list(players_match_dict)
                                player_1_name = self.player_controller.give_player_name(players[0])
                                player_2_name = self.player_controller.give_player_name(players[1])
                                self.match_controller.play_match(player_1_name, player_2_name, match_to_play)

                                tournament.save_tournament()

                        self.round_controller.finish_round(round_to_load)
                        tournament.save_tournament()
                    
                    # Les match n'ot pas été crée (se joue aprés le round repris)
                    if len(matchs_list_to_play) == 0:
                        # to refactoring ==== 
                        current_round = tournament.give_current_round()
                        rounds_to_check = tournament.give_round_list()
                        players = tournament.give_list_players()
                        played_matchs = []
                        for round_to_check in rounds_to_check:

                            matchs_list = self.round_controller.give_list_matchs(round_to_check)
                            for match_in_list in matchs_list:
                                played_matchs.append(match_in_list)
                            
                            played_pairs = []
                            for played_match in played_matchs:
                                players_dict = self.match_controller.give_dict_players(played_match)
                                played_pairs.append(players_dict)
                
                        players = self.shuffle_players(players, current_round, played_pairs)
                        played_pairs_list = list(played_pairs)  # played_pairs est un dictionnaire contenant tous matchs(jouers/score)
                        pairs = self.create_pairs(players, played_pairs_list)
                        print (players)
                        print (played_pairs_list)

                        m = 1
                        for pair in pairs:
                            match_name = "Match_" + str(m)
                            m += 1
                        
                            match = self.match_controller.create_match(match_name, pair[0], pair[1])
                            self.round_controller.add_match(round_to_load, match)
                            tournament.save_tournament()

                        matchs_list_to_play = self.round_controller.give_list_matchs(round_to_load)
                        for match_to_play in matchs_list_to_play:
                            players_match_dict = self.match_controller.give_dict_players(match_to_play)
                            players = list(players_match_dict)
                            player_1_name = self.player_controller.give_player_name(players[0])
                            player_2_name = self.player_controller.give_player_name(players[1])
                            self.match_controller.play_match(player_1_name, player_2_name, match_to_play)

                            tournament.save_tournament()

                        self.round_controller.finish_round(round_to_load)
                        tournament.save_tournament()
            
            date_finish = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            tournament.add_date_finish(date_finish)
            tournament.save_tournament()
            self.classement(tournament, played_pairs)


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
        description = tournament_informations[2]
        round_all_update = tournament_informations[3]
        date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        tournament.modify_start_information(name, place, date_start, description, round_all_update)
        tournament.save_tournament()

        round_all = tournament.give_round_all_information()

        players_list = []
        round_list = []
        current_round = tournament.give_current_round()

        return tournament, players_list, round_list, current_round

    def classement(self, tournament, played_pairs):
        """Classment des joueurs par leur score - du plus élevé au plus petit"""
        players = tournament.give_list_players()
        players.sort(key=lambda p: self.give_player_score(p, played_pairs), reverse=True)

        place = 1
        for player in players:
            score = self.give_player_score(player, played_pairs)
            self.view_tournament.show_classment(player, place, score)
            place += 1

    def give_player_score(self, player, played_pairs):
        """Donne le score d'un joueur"""
        player_score = 0

        for pair in played_pairs:
            for player_in_pair in pair:
                if player_in_pair == player:
                    player_score = int(player_score) + int(pair[player_in_pair])

        return player_score

    def shuffle_players(self, players, current_round, played_pairs):
        """Melange les joueurs"""

        if current_round == 1:
            random.shuffle(players)
        else:
            players.sort(key=lambda p: self.give_player_score(p, played_pairs), reverse=True)  # p reprensent objet Player
        return players
    
    def create_pairs(self, players, played_pairs):
        """Création des paires"""
        players_tmp = players[:]  # players_tmp = players.copy() - même signification
        pairs = []

        for player_1 in players:
            for player_2 in players:
                if player_1 in players_tmp and player_2 in players_tmp:
                    if player_1 != player_2 and not self.check_alredy_played(player_1, player_2, played_pairs):

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

                        pairs.append((player_1, player_2))
                        

        if len(players_tmp) != 0:
            i = 0
            while i < len(players_tmp):
                player_1 = players_tmp[i]
                player_2 = players_tmp[i+1]
                pairs.append((player_1, player_2))
                i += 2

        return pairs

    def check_alredy_played(self, player_1, player_2, played_pairs):
        """Verfication si les joueurs ont déja joué ensemble"""
        for pairs in played_pairs:
            list_played_pairs = list(pairs)
            if player_1 == list_played_pairs[0] or player_1 == list_played_pairs[1]:
                if player_2 == list_played_pairs[0] or player_2 == list_played_pairs[1]:
                    return True

        return False