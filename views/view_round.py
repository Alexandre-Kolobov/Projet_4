"""View round"""


class View_round():
    def show_round_estimation(self, round_all):
        """Confirme la possiblité de faire n round"""
        print("----------------------------------------")
        print(f"Avec ce nombre de joueur il est possible de faire: {round_all} round")

    def show_round_negative_estimation(self, round_all):
        """Confirme l'impossiblité de faire n round"""
        print("----------------------------------------")
        print(f"Avec ce nombre de joueur il n'est pas possible de faire: {round_all} rounds")
        print("Merci d'ajouter d'autres participants")

    def show_round(self, matchs, current_round):
        """Affiche les matchs prevu pour un round"""
        print("----------------------------------------")
        print(f"Voici les matchs du Round {current_round} :")
        for i in matchs:
            print(f"    {i}")

    def get_finish_round(self, round_name):
        """Afiche les actions possibles à la fin d'un round"""
        print("----------------------------------------")
        print(f"Tous les matchs du {round_name} sont joués.")
        print("Que voulez vous faire?")
        print("    1. Continuer le tournois")
        print("    2. Sauvegarder et revenir au menu prencipal")
        print("    3. Sauvegarder et quitter")

        answers = {}

        while True:
            answers = {"Continuer": "1",
                       "Revenir": "2",
                       "Quitter": "3"}
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
