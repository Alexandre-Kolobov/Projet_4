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
        # while True:
        #     print("----------------------------------------")
            # finish_round = input(f"Tous les matchs du {round_name} sont joués. "
            #                      f"Marquer {round_name} comme \"terminé\" (y/n)? ").strip()
            # finish_round = str.lower(finish_round)
            # if finish_round == "y":
            #     return True
            # elif finish_round == "n":
            #     print(f"Merci de marquer le {round_name} comme \"terminé\" pour passer au round suivant.")
        print("----------------------------------------")
        print(f"Tous les matchs du {round_name} sont joués.")
        print("Que voulez vous faire?")
        print("    1. Continuer le tournois")
        print("    2. Sauvegarder et revenir au menu des tournois")
        print("    3. Sauvegarder et quitter")
                                    
        answers = {}

        while True:
            answers = {"Continuer":"1" ,
                       "Revenir":"2",
                       "Quitter":"3"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values():
                for key, item in answers.items():
                    if item == answer:
                        return key
                    
                return key

            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")                    