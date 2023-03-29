"""View"""
from datetime import datetime
import pprint


class View():
    """input from user"""

    def get_tournament_start_informations(self):
        while True:
            name = input("Entrer le titre du tournoi: ")
            if len(name) >= 1:
                break
            else:
                print ("Le titre du tournoi ne dois pas être vide. Merci de le reinsegner.")

        while True:
            place = input("Entrer l'endroit du tournoi: ")
            if len(place) >= 1:
                break
            else:
                print ("L'endroit du tournoi ne dois pas être vide. Merci de le reinsegner.")
        
        
        description = input("Entrer la description du tournoi: ")

        return name, place, description

    def get_player_informations(self):

        while True:
            first_name = input("Tapez le prénom du joueur: ")
            if first_name.isalpha():
                break
            else:
                print ("Le prénom du joueur doit contenir que des lettres et ne pas être vide")
        
        while True:
            family_name = input("Tapez le nom du joueur: ")
            if family_name.isalpha():
                break
            else:
                print ("Le nom du joueur doit contenir que des lettres et ne pas être vide")
        
        while True:
            birth_date = input("Tapez la date de naissance du joueur (DDMMYYYY): ")
            try:
                datetime.strptime(birth_date, "%d%m%Y")
                break
            except (ValueError, TypeError):              
                print ("La date de naissance du joueur doit être au format DDMMYYYY")

        while True:
            add_player = input("Voulez vous ajouter un autre joueur (y/n)? ")
            print("\n")
            add_player = str.lower(add_player)
            if add_player in["y", "n"]:
                break
            else:
                print ("Merci d'indiquer votre choix par (y/n)")
            
        return first_name, family_name, birth_date, add_player

    def add_more_players(self):
        print("Il faut avoir au minimum 2 participants pour povoir lancer le tournois.")
        print("Merci d'ajouter un joueur.")

    def show_players(self, players):
        print("Voici la liste des joueurs participants:")
        for i in players:
            print(i)
    
    def show_round_estimation(self, max_round):
        print("\n")
        print(f"Avec ce nombre de joueur il est possible de faire au maximum: {max_round} rounds")

    def get_round_proposition(self):
        while True:
            round_proposition = input("Merci d'indiquer combien de tours voulez vous jouer: ")
            try:
                int(round_proposition)
                return int(round_proposition)
                break
            except (ValueError, TypeError):              
                print ("Merci d'indiquer un nombre")

    def get_round_proposition_error(self, max_round):
        print(f"Le nombre des tours ne peut pas être superieur à {max_round} rounds")

    def show_round_informations(self, rounds):
        print("Voici la liste des rounds:")
        for i in rounds:
            print(f"{i}: {rounds[i]}")

        


    
