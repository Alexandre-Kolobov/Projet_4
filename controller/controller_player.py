from views.view_tournament import View_tournament
from views.view_player import View_player
from views.view_match import View_match
from views.view_round import View_round
from models.player import Player

class Controller_player:
    def __init__(self):
        # self.tournament = tournament
        self.view_tournament = View_tournament()
        self.view_player = View_player()
        self.view_match = View_match()
        self.view_round = View_round()

    def load_players_from_tournament(self, tournament, players_list):
        if len(players_list) != 0:
            for player in players_list:
                database_players = Player.give_database_players()
                player_name = (player["first_name"] + " " + player["family_name"])
                player_to_load = Player.load_player(player_name)
                player_to_add = Player(player_to_load["first_name"],
                                       player_to_load["family_name"],
                                       player_to_load["birth_date"])
                
                tournament.add_player(player_to_add)
        
        tournament.save_tournament()
    
    def get_players(self, tournament):
        """Création des participants"""

        while True:
            player_name_in_turnament = self.give_players_in_tournament(tournament)
            if len(player_name_in_turnament) != 0:
                self.view_player.show_players(player_name_in_turnament)

            database_players = Player.give_database_players()
            answer = self.view_player.show_menu_player(database_players)

            if answer == "Afficher":
                pass

            if answer == "Selectionner":
                self.select_player(tournament, database_players)

            if answer == "Ajouter":
                self.add_new_player(database_players)

            if answer == "Finir":
                if self.check_number_players(tournament):
                    break

            if answer == "Sauvegarder":
                exit(0)

    def select_player(self, tournament, database_players):
        player_name_in_turnament = self.give_players_in_tournament(tournament)
        selected_player = self.view_player.select_player_from_database(database_players, 
                                                                        player_name_in_turnament)

        if selected_player != None:
            loaded_player = Player.load_player(selected_player)
            loaded_player_to_add = Player(loaded_player["first_name"],
                                          loaded_player["family_name"],
                                          loaded_player["birth_date"])
            tournament.add_player(loaded_player_to_add)
            tournament.save_tournament()

    def add_new_player(self, database_players):
        player_informations = self.view_player.get_player_informations(database_players)

        if player_informations != None:
            first_name = player_informations[0]
            family_name = player_informations[1]
            birth_date = player_informations[2]

            player_to_save = Player(first_name, family_name, birth_date)
            player_to_save.save_player()

    def give_players_in_tournament(self, tournament):
        """Affiche la liste des joueurs en temps réel"""
        players_in_turnament = tournament.give_list_players()
        player_name_in_turnament = []
        for player in players_in_turnament:
            name = player.give_player_name()
            player_name_in_turnament.append(name)
        
        return player_name_in_turnament

    def check_number_players(self, tournament):
        """Verifie la possibilité de jouer le nombre des rounds demandé"""
        participants_len = tournament.give_len_list_players()
        round_all = tournament.give_round_all_information()

        if (participants_len % 2) == 0:  # Si nombre des participant est paire il y a N-1 tours possibles
            max_round = participants_len - 1
            if max_round >= round_all:
                self.view_round.show_round_estimation(round_all)
                return True
            else:
                self.view_round.show_round_negative_estimation(round_all)
                self.get_players(tournament)
        else:  # Si nombre des participant est impaire, il faut ajouter des joueurs
            self.view_round.show_round_negative_estimation(round_all)
            self.get_players(tournament)
