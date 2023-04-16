"""View player"""
from datetime import datetime


class View_player():
    def get_player_informations(self, database_players):
        while True:
            print("----------------------------------------")
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

            player_name_firstname = (first_name + " " + family_name).lower()
            for i in range(len(database_players)):
                database_players[i] = database_players[i].lower()

            if player_name_firstname in database_players:
                print("----------------------------------------")
                print(f"Le joueur {first_name} {family_name} existe déja dans la base des joueurs")
                print("Que voulez vous faire?")
                print("    1. Réessayer le saisie")
                print("    2. Revenir dans le menu des joueurs")

                answers = {"Reessayer":"1" ,
                           "Revenir":"2"}

                answer = input("Votre choix: ").strip()

                if answer in answers.values() and answer == answers["Reessayer"]:
                    pass

                elif answer in answers.values() and answer == answers["Revenir"]:
                    print("----------------------------------------")
                    print("Retour au menu des joueurs")
                    return None
            else:
                print(f"Le joueur {first_name} {family_name} a été ajouté dans la base des joueurs")
                return first_name, family_name, birth_date

    def show_players(self, players):
        print("----------------------------------------")
        print("Voici la liste des joueurs participants:")
        for i in players:
            print(i)

    def show_player_score(self, player, score):
        print (f"{player} - {score}")

    def show_menu_player(self, database_players):
        print("----------------------------------------")
        print("Menu des joueurs:")
        print("    1. Afficher la liste des joueurs existants dans la base")
        print("    2. Sélectionner un joueur dans la base des joueurs existants pour l'ajouter au tournois")
        print("    3. Ajouter un nouveau joueur dans la base des joueurs")
        print("    4. Finir la selection des joueurs")
        print("    5. Sauvegarder et quitter")
        answers = {}

        while True:
            answers = {"Afficher":"1" ,
                       "Selectionner":"2",
                       "Ajouter":"3",
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

                for key, item in answers.items():
                    if item == answer:
                        return key

                return key
                # print("----------------------------------------")
                # print("Menu des joueurs:")
                # print("    1. Afficher la liste des joueurs existants dans la base")
                # print("    2. Sélectionner un joueur dans la base des joueurs existants pour l'ajouter au tournois")
                # print("    3. Ajouter un nouveau joueur dans la base des joueurs")
                # print("    4. Finir la selection des joueurs")
                # print("    5. Sauvegarder et quitter")

            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")

    def select_player_from_database(self, database_players, player_name_in_turnament):
        """Selectionne un joueur dans la db et verifie s'il ne participe pas déja dans ce tournois"""
        while True:
            print("----------------------------------------")
            print("Voici la list des joueurs existants dans la base:")

            for player in database_players:
                print(player)

            print("----------------------------------------")
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
                    return None
                else:
                    answers_list = []
                    for i in answers.values():
                        answers_list.append(i)
                    answers_list.sort()
                    print(f"Merci de reesayer en choissisant parmis {answers_list}")
            else:
                return player_selected
