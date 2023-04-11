"""View player"""
from datetime import datetime


class View_player():
    def get_player_informations(self):

        while True:
            first_name = input("Tapez le prénom du joueur: ").strip()
            if first_name.isalpha():
                break
            else:
                print("Le prénom du joueur doit contenir que des lettres et ne pas être vide")

        while True:
            family_name = input("Tapez le nom du joueur: ").strip()
            if family_name.isalpha():
                break
            else:
                print("Le nom du joueur doit contenir que des lettres et ne pas être vide")

        while True:
            birth_date = input("Tapez la date de naissance du joueur (DDMMYYYY): ").strip()
            try:
                datetime.strptime(birth_date, "%d%m%Y")
                break
            except (ValueError, TypeError):
                print("La date de naissance du joueur doit être au format DDMMYYYY")

        while True:
            add_player = input("Voulez vous ajouter un autre joueur (y/n)? ").strip()
            print("\n")
            add_player = str.lower(add_player)
            if add_player in ["y", "n"]:
                break
            else:
                print("Merci d'indiquer votre choix par (y/n)")

        return first_name, family_name, birth_date, add_player

    def show_players(self, players):
        print("\n")
        print("Voici la liste des joueurs participants:")
        for i in players:
            print(i)

    def show_player_score(self, player, score):
        print (f"{player} - {score}")