"""View round"""


class View_round():
    def show_round_estimation(self, round_all):
        print("----------------------------------------")
        print(f"Avec ce nombre de joueur il est possible de faire: {round_all} round")

    def show_round_negative_estimation(self, round_all):
        print("----------------------------------------")
        print(f"Avec ce nombre de joueur il n'est pas possible de faire: {round_all} rounds")
        print("Merci d'ajouter d'autres participants")

    def show_round(self, matchs, current_round):
        print("----------------------------------------")
        print(f"Voici les matchs prevu pour le Round {current_round} :")
        for i in matchs:
            print(i)

    def get_finish_round(self, round_name):
        while True:
            print("----------------------------------------")
            finish_round = input(f"Tous les matchs du {round_name} sont joués. "
                                 f"Marquer {round_name} comme \"terminé\" (y/n)? ").strip()
            finish_round = str.lower(finish_round)
            if finish_round == "y":
                return True
            elif finish_round == "n":
                print(f"Merci de marquer le {round_name} comme \"terminé\" pour passer au round suivant.")
