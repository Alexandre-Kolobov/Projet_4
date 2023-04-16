from views.view_tournament import View_tournament
from views.view_player import View_player
from views.view_match import View_match
from views.view_round import View_round
from models.player import Player

class Controller_player:
    def __init__(self, tournament):
        self.tournament = tournament
        self.view_tournament = View_tournament()
        self.view_player = View_player()
        self.view_match = View_match()
        self.view_round = View_round()
    
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

        # TEST
        player_1 = Player("a", "a", "05101992")
        self.tournament.add_player(player_1)
        player_1.save_player()

        player_2 = Player("b", "b", "05101992")
        self.tournament.add_player(player_2)
        player_2.save_player()

        player_3 = Player("c", "c", "05101992")
        self.tournament.add_player(player_3)
        player_3.save_player()

        player_4 = Player("d", "d", "05101992")
        self.tournament.add_player(player_4)
        player_4.save_player()

        player_5 = Player("e", "e", "05101992")
        self.tournament.add_player(player_5)
        player_5.save_player()

        player_6 = Player("f", "f", "05101992")
        self.tournament.add_player(player_6)
        player_6.save_player()

        while True:
            player_name_in_turnament = self.give_players_in_tournament()
            if len(player_name_in_turnament) != 0:
                self.view_player.show_players(player_name_in_turnament)

            database_players = Player.give_database_players()
            answer = self.view_player.show_menu_player(database_players)

            if answer == "Afficher":
                pass

            if answer == "Selectionner":
                player_name_in_turnament = self.give_players_in_tournament()
                selected_player = self.view_player.select_player_from_database(database_players, 
                                                                               player_name_in_turnament)

                if selected_player != None:
                    loaded_player = Player.load_player(selected_player)
                    self.tournament.add_player(loaded_player)
                    self.tournament.save_tournament()

            if answer == "Ajouter":
                player_informations = self.view_player.get_player_informations(database_players)

                if player_informations != None:
                    first_name = player_informations[0]
                    family_name = player_informations[1]
                    birth_date = player_informations[2]

                    player_to_save = Player(first_name, family_name, birth_date)
                    player_to_save.save_player()

            if answer == "Finir":
                break

            if answer == "Sauvegarder":
                exit(0)

    def check_number_players(self):
        participants = self.tournament.give_list_players()
        print(participants)
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
