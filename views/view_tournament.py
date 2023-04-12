"""View tournament"""


class View_tournament():
    def get_tournament_start_informations(self, round_all):
        while True:
            name = input("Entrer le titre du tournoi: ").strip()
            if len(name) >= 1:
                break
            else:
                print("Le titre du tournoi ne dois pas être vide. Merci de le reinsegner.")

        while True:
            place = input("Entrer l'endroit du tournoi: ").strip()
            if len(place) >= 1:
                break
            else:
                print("L'endroit du tournoi ne dois pas être vide. Merci de le reinsegner.")

        description = input("Entrer la description du tournoi: ").strip()

        round = input(f"Voulez vous changer le nombre de round qui est {round_all} par defaut "
                        "(y/n)?").strip().lower()
        while True:
            if round == "y":
                round_all = input("Combien de round voulez vous jouer?")
                try:
                    int(round_all)
                    break
                except ValueError:
                    print("Merci d'entrer un nombre.")
            elif round =="n":
                break
            else:
                round = input(f"Voulez vous changer le nombre de round qui est {round_all} par defaut "
                                "(y/n)?").strip().lower()

        return name, place, description, round_all

    def show_classment(self, player, place, score):
        if place == 1:
            print("Voici le classement du tournois:")
            print(f"Place {place}: {player} - score {score}")
        else:
            print(f"Place {place}: {player} - score {score}")
