from views.view_round import View_round
from models.round import Round


class Controller_round:
    def __init__(self):
        self.view_round = View_round()

    def create_round(self, round_name):
        """Création des rounds vides"""
        round = Round(name=round_name)
        return round

    def load_round(self, round):
        """Chargement d'un round"""
        round_to_load = Round(name=round["name"],
                              date_start=round["date_start"],
                              date_finish=round["date_finish"],
                              finish_status=round["finish_status"])

        matchs = round["matchs"]
        return round_to_load, matchs

    def finish_round(self, round):
        """Les actions à réaliser à la fin d'un round"""
        round_name = round.give_round_name()
        answer = self.view_round.get_finish_round(round_name)
        if answer == "Continuer":
            round.update_finish_status(True)

        if answer == "Revenir":
            return False

        if answer == "Quitter":
            exit(0)

    def give_list_matchs(self, round):
        """Return un list des match pour un round"""
        matchs_list = round.give_match_list()
        return matchs_list

    def add_match(self, round, match):
        """Ajout un match pour un round"""
        round.add_match(match)

    def check_finish_status(self, round):
        """Verification si le round est fini"""
        return round.give_finish_status()

    def show_matchs(self, matchs_list_to_play, current_round):
        """Affiche les matchs d'un round"""
        self.view_round.show_round(matchs_list_to_play, current_round)
