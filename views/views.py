"""View"""
from datetime import datetime
import pprint


class View():
    """input from user"""

    def get_tournament_start_informations(self):
        while True:
            name = input("Entrer le titre du tournoi: ").strip()
            if len(name) >= 1:
                break
            else:
                print ("Le titre du tournoi ne dois pas être vide. Merci de le reinsegner.")

        while True:
            place = input("Entrer l'endroit du tournoi: ").strip()
            if len(place) >= 1:
                break
            else:
                print ("L'endroit du tournoi ne dois pas être vide. Merci de le reinsegner.")
        
        
        description = input("Entrer la description du tournoi: ").strip()

        return name, place, description

    def get_player_informations(self):

        while True:
            first_name = input("Tapez le prénom du joueur: ").strip()
            if first_name.isalpha():
                break
            else:
                print ("Le prénom du joueur doit contenir que des lettres et ne pas être vide")
        
        while True:
            family_name = input("Tapez le nom du joueur: ").strip()
            if family_name.isalpha():
                break
            else:
                print ("Le nom du joueur doit contenir que des lettres et ne pas être vide")
        
        while True:
            birth_date = input("Tapez la date de naissance du joueur (DDMMYYYY): ").strip()
            try:
                datetime.strptime(birth_date, "%d%m%Y")
                break
            except (ValueError, TypeError):              
                print ("La date de naissance du joueur doit être au format DDMMYYYY")

        while True:
            add_player = input("Voulez vous ajouter un autre joueur (y/n)? ").strip()
            print("\n")
            add_player = str.lower(add_player)
            if add_player in["y", "n"]:
                break
            else:
                print ("Merci d'indiquer votre choix par (y/n)")
            
        return first_name, family_name, birth_date, add_player

    def show_players(self, players):
        print("\n")
        print("Voici la liste des joueurs participants:")
        for i in players:
            print(i)
    
    def add_player_repos(self):
        print("\n")
        print("Comme le nombre des joueurs est impaires, nous ajoutons un joueur fictif.")
        print("Ce joueur donne doroit à la victoire automatiqeu pour celui qui joue avec.")


    def show_round_estimation(self, round_all):
        print("\n")
        print(f"Avec ce nombre de joueur il est possible de faire: {round_all} rounds")

    def show_round_negative_estimation(self, round_all):
        print("\n")
        print(f"Avec ce nombre de joueur il n'est pas possible de faire: {round_all} rounds")
        print("Merci d'ajouter d'autres participants")

    def get_round_proposition(self):
        while True:
            round_proposition = input("Merci d'indiquer combien de tours voulez vous jouer: ").strip()
            try:
                int(round_proposition)
                return int(round_proposition)
                break
            except (ValueError, TypeError):              
                print ("Merci d'indiquer un nombre")

    def get_round_proposition_error(self, max_round):
        print(f"Le nombre des tours ne peut pas être égale à 0 ou superieur à {max_round} rounds")

    def show_round(self, matchs, name):
        print(f"Voici les paires dans {name}:")
        for i in matchs:
            print(i)

    def update_player_1_score(self, player_1):
        while True:
            score_1 = input(f"Entrer le score du joueur {player_1} (0 - perdant, 0.5 - égalité, 1 - gagnant): ").strip()
            if int(score_1) in [0, 0.5, 1]:
                break
            else:
                print(f"Merci de rentrer le score du joueur {player_1} correctemment.")
        
        return score_1

    def play_match(self, player_1_name, player_2_name):
        print("\n")
        print(f"{player_1_name} et {player_2_name} jouent.")
        while True:
            match_result = input("Entrer nom et prenom du gagnat ou \"égalité\": ").strip()
            if match_result in [player_1_name, player_2_name, "égalité"]:
                break
            else:
                print(f"Le resultat n'a pas été entré correctemment. Merci de reesayer.")

        return match_result
    
    def show_classment(self, player, place, score):
        if place == 1:
            print("Voici le classement du tournois:")
            print (f"Place {place}: {player} - score {score}")
        else:
            print (f"Place {place}: {player} - score {score}")
