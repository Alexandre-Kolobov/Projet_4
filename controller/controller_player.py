from views.view_player import View_player
from models.player import Player


class Controller_player:
    def __init__(self):
        self.view_player = View_player()

    def load_players_from_tournament(self, player):
        """Chargement d'un joueur dans une instance de classe"""
        player_name = ("p" + str(player["counter"]))
        player_to_load = Player.load_player(player_name)

        player_to_add = Player(player_to_load["first_name"],
                               player_to_load["family_name"],
                               player_to_load["birth_date"],
                               player_to_load["counter"])

        return player_to_add

    def players_menu(self):
        database_players = Player.give_database_players()
        answer = self.view_player.show_menu_players(database_players)

        return answer

    def get_player(self, players_in_turnament):
        """Création des participants"""

        player_name_in_turnament = self.give_players_in_tournament(players_in_turnament)
        database_players = Player.give_database_players()
        answer = self.view_player.show_menu_tournament(database_players, player_name_in_turnament)

        return answer

    def select_player(self, players_in_turnament):
        """Selection d'un joueur à partir de la base des données"""
        player_name_in_turnament = self.give_players_in_tournament(players_in_turnament)
        if len(player_name_in_turnament) != 0:
            self.view_player.show_players(player_name_in_turnament)

        database_players = Player.give_database_players()
        selected_players = self.view_player.select_player_from_database(database_players,
                                                                        player_name_in_turnament)
        loaded_players_list = []
        for player in selected_players:
            loaded_player = Player.load_player(player)
            loaded_player_to_add = Player(loaded_player["first_name"],
                                          loaded_player["family_name"],
                                          loaded_player["birth_date"],
                                          loaded_player["counter"])

            loaded_players_list.append(loaded_player_to_add)
        return loaded_players_list

    def add_one_more_player(self):
        """Demande de selectionenr un joueur supplementaire"""
        answer = self.view_player.add_one_more_player()
        return answer

    def add_new_player(self):
        """Création d'un nouveau joueur"""
        counter = Player.load_counter()
        database_players = Player.give_database_players()
        player_informations = self.view_player.get_player_informations(database_players, counter)

        if player_informations is not None:
            first_name = player_informations[0]
            family_name = player_informations[1]
            birth_date = player_informations[2]
            player_to_save = Player(first_name, family_name, birth_date, counter)
            player_to_save.save_player()
        Player.increment_counter()

        return player_to_save

    def add_one_more_new_player(self):
        """Demande d'ajouter' un joueur supplementaire"""
        answer = self.view_player.add_one_more__new_player()
        return answer

    def give_players_in_tournament(self, players_in_turnament):
        """Affiche la liste des joueurs en temps réel"""
        player_name_in_turnament = []
        for player in players_in_turnament:
            name = player.give_player_name()
            player_name_in_turnament.append(name)

        return player_name_in_turnament

    def player_name_to_check(self, player_name, player):
        """Verfication d'un nom sous forme de string avec une instace de classe player"""
        if player_name == player.give_player_name():
            return player

    def give_player_name(self, player):
        """Donne le nom d'un joueur"""
        return player.give_player_name()

    def give_database_players(self):
        """Donne la liste des joueurs dans la base"""
        database_players = Player.give_database_players()
        return database_players

    def show_players(self, players_in_turnament):
        """Affiche la liste des joueurs participants au tournoi"""
        player_name_in_turnament = self.give_players_in_tournament(players_in_turnament)
        if len(player_name_in_turnament) != 0:
            self.view_player.show_players(player_name_in_turnament)
