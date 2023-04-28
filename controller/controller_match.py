from views.view_match import View_match
from models.match import Match


class Controller_match:
    def __init__(self):
        self.view_match = View_match()

    def create_match(self, match_name, player_1, player_2):
        """Création de match"""
        match = Match(match_name, player_1, player_2)
        return match

    def play_match(self, player_1_name, player_2_name, match):
        """Joue le match"""

        match_result = self.view_match.play_match(player_1_name, player_2_name)
        match.update_match_score(player_1_name, player_2_name, match_result)

        player_1_score = match.give_player_1_score()
        player_2_score = match.give_player_2_score()

        self.view_match.show_match_result(player_1_name, player_2_name, player_1_score, player_2_score)

    def load_match(self, player_1, player_2, match):
        """Chargement d'un match"""
        match_to_load = Match(name=match["name"],
                              player_1=player_1,
                              player_2=player_2,
                              score_1=match["score_1"],
                              score_2=match["score_2"])
        return match_to_load

    def players_names_to_check(self, match):
        """Création du nom de joueur à partir d'un dictionnaire"""
        p1_first_name = match['player_1']['first_name']
        p1_family_name = match['player_1']['family_name']
        p1_id = "id" + str(match['player_1']['counter'])

        p2_first_name = match['player_2']['first_name']
        p2_family_name = match['player_2']['family_name']
        p2_id = "id" + str(match['player_2']['counter'])

        player_1_to_load = p1_first_name + " " + p1_family_name + " " + p1_id
        player_2_to_load = p2_first_name + " " + p2_family_name + " " + p2_id

        return player_1_to_load, player_2_to_load

    def give_dict_players(self, match):
        """Return un dictionanire avec joueurs et leur score par match"""
        player_1 = match.give_player_1()
        player_1_score = match.give_player_1_score()
        player_2 = match.give_player_2()
        player_2_score = match.give_player_2_score()
        players = {player_1: player_1_score, player_2: player_2_score}
        return players

    def check_if_match_played(self, match):
        """Verfification si un match a déja été joué"""
        return match.check_if_match_played()

    def finish_match(self):
        """Action à faire à la fin d'un match"""
        answer = self.view_match.get_finish_match()
        if answer == "Oui":
            pass

        if answer == "Revenir":
            return False

        if answer == "Quitter":
            exit(0)
