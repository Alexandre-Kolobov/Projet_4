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

    def show_menu_player(self, database_players):
        print("----------------------------------------")
        print("Menu des joueurs:")
        print("    1. Afficher la liste des joueurs existants dans la base")
        print("    2. Sélectionner les joueurs dans la liste des joueurs existants")
        print("    3. Créer un nouveau joueur")
        print("    4. Finir la création des joueurs")
        print("    5. Sauvegarder et quitter")
        answers = {}

        while True:
            answers = {"Afficher":"1" ,
                       "Selectionner":"2",
                       "Creer":"3",
                       "Finir":"4", 
                       "Sauvegarder":"5"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values() and answer != answers["Afficher"]:
                for key, item in answers.items():
                    if item == answer:
                        return key
            
            elif answer in answers.values() and answer == answers["Afficher"]:
                print("----------------------------------------")
                print("Voici la list des joueurs existants dans la base:")

                for player in database_players:
                    print(player)

                print("----------------------------------------")
                print("Menu des joueurs:")
                print("    1. Afficher la liste des joueurs existants dans la base")
                print("    2. Sélectionner les joueurs dans la liste des joueurs existants")
                print("    3. Créer un nouveau joueur")
                print("    4. Finir la création des joueurs")
                print("    5. Sauvegarder et quitter")

            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")

    def select_player_from_database(self, database_players, player_name_in_turnament):
        while True:
            print("----------------------------------------")
            print("Voici la list des joueurs existants dans la base:")

            for player in database_players:
                print(player)

            player_selected = input("Merci de selectionner un joueur: ").strip()
            for i in range(len(player_name_in_turnament)):
                player_name_in_turnament[i] = player_name_in_turnament[i].lower()

            if player_selected.lower() in player_name_in_turnament:
                print("----------------------------------------")
                print(f"Le joueur {player_selected} participe déja à ce tournois")
                print("Voulez vous selectionner un autre joueur?")
                print("----------------------------------------")
                print("    1. Oui")
                print("    2. Non")

                answers = {"Oui":"1" ,
                           "Non":"2"}
                
                answer = input("Votre choix: ").strip()
                if answer in answers.values() and answer == answers["Oui"]:
                    pass

                elif answer in answers.values() and answer == answers["Non"]:
                    print("----------------------------------------")
                    print("Retour au menu des joueurs")
                    break
                else:
                    answers_list = []
                    for i in answers.values():
                        answers_list.append(i)
                    answers_list.sort()
                    print(f"Merci de reesayer en choissisant parmis {answers_list}")
            else:
                return player_selected
