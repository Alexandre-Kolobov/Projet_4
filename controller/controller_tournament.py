from views.view_tournament import View_tournament
from views.view_rapport import View_rapport
from models.tournament import Tournament
from datetime import datetime
import random


class Controller_tournament:
    def __init__(self, player_controller, round_controller, match_controller):
        # self.tournament = Tournament()
        self.view_tournament = View_tournament()
        self.view_rapport = View_rapport()
        self.player_controller = player_controller
        self.round_controller = round_controller
        self.match_controller = match_controller

    def run(self):
        """Lance le programme"""
        tournament_informations = self.main_menu()
        tournament = tournament_informations[0]
        players_list = tournament_informations[1]
        round_list = tournament_informations[2]
        current_round = tournament_informations[3]
        # self.tournament_status(tournament)

        # On charge les joueurs s'ils existent dans le tournois
        if len(players_list) != 0:
            for player in players_list:
                player_to_add = self.player_controller.load_players_from_tournament(player)
                tournament.add_player(player_to_add)
                tournament.save_tournament()

        #  Si les rounds n'ont pas été commencé (on continue la création des joueurs)
        if current_round == 0:
            while True:
                self.tournament_status(tournament)
                players_in_turnament = tournament.give_list_players()
                answer = self.player_controller.get_player(players_in_turnament)

                if answer == "Ajouter":
                    player = self.player_controller.select_player(players_in_turnament)

                    if player is not None:
                        tournament.add_player(player)
                        tournament.save_tournament()

                        while True:
                            answer_one_more = self.player_controller.add_one_more_player()
                            if answer_one_more == "Oui":
                                player = self.player_controller.select_player(players_in_turnament)
                                if player is not None:
                                    tournament.add_player(player)
                                    tournament.save_tournament()
                                else:
                                    break
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
                self.round_controller.update_start_round_date(round)
                if self.round_controller.give_round_name(round) == "Round_1":
                    date_start_real = self.round_controller.give_round_date_start(round)
                    tournament.update_start_date(date_start_real)

                tournament.update_current_round()
                tournament.save_tournament()
                self.tournament_status(tournament)
                players = tournament.give_list_players()
                current_round = tournament.give_current_round()
                played_pairs = self.played_pairs(tournament)

                players = self.shuffle_players(players, current_round, played_pairs)
                # played_pairs est un dictionnaire contenant tous matchs(jouers/score)
                played_pairs_list = list(played_pairs)
                pairs = self.create_pairs(players, played_pairs_list)

                m = 1
                for pair in pairs:
                    match_name = "Match_" + str(m)
                    m += 1

                    match = self.match_controller.create_match(match_name, pair[0], pair[1])
                    self.round_controller.add_match(round, match)
                    tournament.save_tournament()

                matchs_list_to_play = self.round_controller.give_list_matchs(round)
                self.round_controller.show_matchs(matchs_list_to_play, current_round)
                for match_to_play in matchs_list_to_play:
                    players_match_dict = self.match_controller.give_dict_players(match_to_play)
                    players = list(players_match_dict)

                    player_1_name = self.player_controller.give_player_name(players[0])
                    player_2_name = self.player_controller.give_player_name(players[1])

                    self.match_controller.play_match(player_1_name, player_2_name, match_to_play)
                    tournament.save_tournament()

                    if match_to_play != matchs_list_to_play[-1]:
                        if self.match_controller.finish_match() is False:
                            return True

                if self.round_controller.finish_round(round) is False:
                    return True

                tournament.save_tournament()

            date_finish = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            tournament.add_date_finish(date_finish)
            tournament.save_tournament()

        else:
            matchs_par_round = {}
            for round in round_list:
                round_informations = self.round_controller.load_round(round)
                round_to_load = round_informations[0]
                matchs = round_informations[1]
                matchs_par_round[round_to_load] = matchs
                tournament.add_round(round_to_load)
                tournament.save_tournament()

            rounds = tournament.give_round_list()
            for round in rounds:
                matchs = matchs_par_round[round]
                for match in matchs:
                    players = tournament.give_list_players()
                    players_names = self.match_controller.players_names_to_check(match)
                    player_1_name = players_names[0]
                    player_2_name = players_names[1]
                    for player in players:
                        if self.player_controller.player_name_to_check(player_1_name, player) is not None:
                            player_1 = self.player_controller.player_name_to_check(player_1_name, player)
                        if self.player_controller.player_name_to_check(player_2_name, player) is not None:
                            player_2 = self.player_controller.player_name_to_check(player_2_name, player)

                    loaded_match = self.match_controller.load_match(player_1, player_2, match)
                    self.round_controller.add_match(round, loaded_match)
                    tournament.save_tournament()

                if self.round_controller.check_finish_status(round) is False:
                    matchs_list_to_play = self.round_controller.give_list_matchs(round)
                    self.round_controller.show_matchs(matchs_list_to_play, round)
                    # Continuer tournament à partir d'un round (les matchs sont crées mais pas joués compeltement)
                    if len(matchs_list_to_play) != 0:
                        matchs_list_to_play = self.round_controller.give_list_matchs(round)
                        for match_to_play in matchs_list_to_play:

                            if self.match_controller.check_if_match_played(match_to_play) is False:
                                players_match_dict = self.match_controller.give_dict_players(match_to_play)
                                players = list(players_match_dict)
                                player_1_name = self.player_controller.give_player_name(players[0])
                                player_2_name = self.player_controller.give_player_name(players[1])
                                self.match_controller.play_match(player_1_name, player_2_name, match_to_play)

                                tournament.save_tournament()

                                if match_to_play != matchs_list_to_play[-1]:
                                    if self.match_controller.finish_match() is False:
                                        return True

                        if self.round_controller.finish_round(round) is False:
                            return True
                        tournament.save_tournament()

                    # Les match n'ont pas été crée (se joue aprés le round repris)
                    if len(matchs_list_to_play) == 0:
                        current_round = tournament.give_current_round()
                        players = tournament.give_list_players()
                        played_pairs = self.played_pairs(tournament)
                        players = self.shuffle_players(players, current_round, played_pairs)
                        # played_pairs est un dictionnaire contenant tous matchs(jouers/score)
                        played_pairs_list = list(played_pairs)
                        pairs = self.create_pairs(players, played_pairs_list)

                        m = 1
                        for pair in pairs:
                            match_name = "Match_" + str(m)
                            m += 1

                            match = self.match_controller.create_match(match_name, pair[0], pair[1])
                            self.round_controller.add_match(round, match)
                            tournament.save_tournament()

                        matchs_list_to_play = self.round_controller.give_list_matchs(round)
                        self.round_controller.show_matchs(matchs_list_to_play, round)
                        for match_to_play in matchs_list_to_play:
                            players_match_dict = self.match_controller.give_dict_players(match_to_play)
                            players = list(players_match_dict)
                            player_1_name = self.player_controller.give_player_name(players[0])
                            player_2_name = self.player_controller.give_player_name(players[1])
                            self.match_controller.play_match(player_1_name, player_2_name, match_to_play)

                            tournament.save_tournament()

                            if match_to_play != matchs_list_to_play[-1]:
                                if self.match_controller.finish_match() is False:
                                    return True

                        if self.round_controller.finish_round(round) is False:
                            return True
                        tournament.save_tournament()

            tournament_status_dict = tournament.tournament_status()
            if tournament_status_dict["date_finish"] == "":
                date_finish = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                tournament.add_date_finish(date_finish)
                tournament.save_tournament()

        played_pairs = self.played_pairs(tournament)
        self.classement(tournament, played_pairs)

        self.tournament_finish_informations(tournament)

    def main_menu(self):
        """Initialise un tournois"""
        while True:
            database_tournois = Tournament.give_database_tournaments()
            tournois_info_dict = {}
            for tournois in database_tournois:
                tournois_info = Tournament.load_tournament(tournois)
                tournois_info_dict[tournois] = tournois_info

            answer = self.view_tournament.show_main_manu()
            if answer == "Rapports":
                while True:
                    database_players = self.player_controller.give_database_players()
                    answer_rapport = self.view_rapport.show_menu_rapports(database_tournois,
                                                                          database_players,
                                                                          tournois_info_dict)
                    if answer_rapport == "Details":
                        select_tournament = self.view_rapport.select_tournament(database_tournois,
                                                                                tournois_info_dict)
                        if select_tournament is not None:
                            while True:
                                answer_details = self.view_rapport.show_menu_details(tournois_info_dict,
                                                                                     select_tournament)
                                if answer_details == "Revenir":
                                    break

                                if answer_details == "Quitter":
                                    exit(0)

                    if answer_rapport == "Revenir":
                        break

                    if answer_rapport == "Quitter":
                        exit(0)
            
            if answer == "Joueurs":
                while True:
                    answer_player = self.player_controller.players_menu()
                    if answer_player == "Ajouter":
                        self.player_controller.add_new_player()

                        while True:
                            answer_one_more = self.player_controller.add_one_more_new_player()
                            if answer_one_more == "Oui":
                                self.player_controller.add_new_player()
                            else:
                                break

                    if answer_player == "Revenir":
                        break

                    if answer_player == "Quitter":
                        exit(0)

            if answer == "Tournois":
                while True:
                    answer_tournament = self.view_tournament.show_tournament_menu()
                    if answer_tournament == "Reprendre":
                        tournament_informations = self.load_tournament(database_tournois, tournois_info_dict)
                        return tournament_informations

                    if answer_tournament == "Creer":
                        tournament_informations = self.new_tournament(database_tournois)
                        return tournament_informations
                    
                    if answer_tournament == "Revenir":
                        break

                    if answer_tournament == "Quitter":
                        exit(0)

            if answer == "Quitter":
                exit(0)

    def load_tournament(self, database_tournois, tournois_info_dict):
        """Charge un tournois"""
        selected_tournament = self.view_tournament.select_tournament_from_database(database_tournois,
                                                                                   tournois_info_dict)

        if selected_tournament is not None:
            selected_to_load_tournament = Tournament.load_tournament(selected_tournament)
            tournament = Tournament(name=selected_to_load_tournament["name"],
                                    place=selected_to_load_tournament["place"],
                                    date_start=selected_to_load_tournament["date_start"],
                                    date_finish=selected_to_load_tournament["date_finish"],
                                    round_all=selected_to_load_tournament["round_all"],
                                    round_current=selected_to_load_tournament["round_current"],
                                    description=selected_to_load_tournament["description"],
                                    date_start_schedule = selected_to_load_tournament["date_start_schedule"],
                                    date_finish_schedule = selected_to_load_tournament["date_finish_schedule"])

            players_list = selected_to_load_tournament["players_list"]
            round_list = selected_to_load_tournament["round_list"]
            current_round = selected_to_load_tournament["round_current"]
            return tournament, players_list, round_list, current_round

    def new_tournament(self, database_tournois):
        """Créer un nouveau tournois"""
        tournament = Tournament()
        round_all = tournament.give_round_all_information()
        tournament_informations = self.view_tournament.get_tournament_start_informations(round_all, database_tournois)
        name = tournament_informations[0]
        place = tournament_informations[1]
        description = tournament_informations[2]
        round_all_update = tournament_informations[3]
        date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        date_start_schedule  = tournament_informations[4]
        date_finish_schedule = tournament_informations[5]

        tournament.modify_start_information(name, place, date_start, description, round_all_update, date_start_schedule, date_finish_schedule)
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
                    player_score = float(player_score) + float(pair[player_in_pair])

        return player_score

    def shuffle_players(self, players, current_round, played_pairs):
        """Melange les joueurs"""
        if current_round == 1:
            random.shuffle(players)
        else:
            # p reprensent objet Player
            players.sort(key=lambda p: self.give_player_score(p, played_pairs), reverse=True)
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

    def tournament_status(self, tournament):
        """Affiche le statut d'un tournois en temps réel"""
        tournament_status_dict = tournament.tournament_status()
        tournament_name = tournament_status_dict["name"]
        tournament_start = tournament_status_dict["date_start"]
        tournament_finish = tournament_status_dict["date_finish"]
        tournament_round_current = tournament_status_dict["round_current"]
        tournament_round_all = tournament_status_dict["round_all"]
        tournament_start_shedule = tournament_status_dict["date_start_schedule"]
        tournament_finish_shedule = tournament_status_dict["date_finish_schedule"]

        self.view_tournament.tournament_status(tournament_name,
                                               tournament_start,
                                               tournament_finish,
                                               tournament_round_current,
                                               tournament_round_all,
                                               tournament_start_shedule,
                                               tournament_finish_shedule)

    def played_pairs(self, tournament):
        """Return unen liste des paires déja joué dans le tournoi"""
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

        return played_pairs

    def tournament_finish_informations(self, tournament):
        """Les actions à la fin d'un tournois"""
        while True:
            answer = self.view_tournament.show_menu_post_tournament()
            if answer == "Joueurs":
                players_in_turnament = tournament.give_list_players()
                self.player_controller.show_players(players_in_turnament)

            if answer == "Matchs":
                rounds_to_check = tournament.give_round_list()

                for round_to_check in rounds_to_check:
                    matchs_list = self.round_controller.give_list_matchs(round_to_check)
                    self.round_controller.show_matchs(matchs_list, round_to_check)

            if answer == "Revenir":
                return True

            if answer == "Quitter":
                exit(0)
