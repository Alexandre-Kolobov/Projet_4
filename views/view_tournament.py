"""View tournament"""


class View_tournament():
    def get_tournament_start_informations(self):
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

        return name, place, description

    def show_classment(self, player, place, score):
        if place == 1:
            print("Voici le classement du tournois:")
            print(f"Place {place}: {player} - score {score}")
        else:
            print(f"Place {place}: {player} - score {score}")
