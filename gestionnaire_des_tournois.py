# import json
from models.tournament import Tournament
from controller.controller import Controller


class Club:
    def __init__(self, id):
        self.id = id  # l'identifiant national d’échecs

def main():
    # test = Controller()
    # test.create_pairs()
    # test.play_game()

    tournament_instance = Tournament(name = "T1", place = "Paris", date_start = "14082023")
    # round_estimation = Controller().round_estimation()
    # round_proposition = Controller().round_proposition(round_estimation)
    
    tournament = Controller()
    round_estimation = tournament.round_estimation()
    tournament.round_proposition(round_estimation)

main()
