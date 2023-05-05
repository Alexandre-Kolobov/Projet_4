"""View player"""
from datetime import datetime
import re


class View_player():
    def get_player_informations(self, database_players, counter):
        """Recuprer les infos d'un joueur à créer"""
        while True:
            print("----------------------------------------")
            while True:
                first_name = input("Entrer le prénom du joueur: ").strip()
                if first_name.isalpha():
                    break
                else:
                    print("Le prénom du joueur doit contenir que des lettres et ne pas être vide")

            while True:
                family_name = input("Entrer le nom du joueur: ").strip()
                if family_name.isalpha():
                    break
                else:
                    print("Le nom du joueur doit contenir que des lettres et ne pas être vide")

            while True:
                birth_date = input("Entrer la date de naissance du joueur (DDMMYYYY): ").strip()
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
                print("Que voulez-vous faire?")
                print("    1. Réessayer le saisie")
                print("    2. Revenir dans le menu des joueurs")

                answers = {"Reessayer": "1",
                           "Revenir": "2"}

                answer = input("Votre choix: ").strip()

                if answer in answers.values() and answer == answers["Reessayer"]:
                    pass

                elif answer in answers.values() and answer == answers["Revenir"]:
                    print("----------------------------------------")
                    print("Retour au menu des joueurs")
                    return None
            else:
                print(f"Le joueur {first_name} {family_name} "
                      "a été ajouté dans la base des joueurs avec identifiant p{counter}")
                return first_name, family_name, birth_date

    def show_players(self, players):
        """Affiche les joueur participants"""
        print("----------------------------------------")
        if len(players) > 0:
            print("Voici la liste des joueurs participant:")
            sorted_players = sorted(players)
            for i in sorted_players:
                print(f"    {i}")
        else:
            print("Aucun joueur ne participe au tournoi")

    def show_menu_tournament(self, database_players, players_in_turnament):
        """Affiche le menu du tournoi"""
        print("----------------------------------------")
        print("Menu du tournoi:")
        print("    1. Afficher la liste des joueurs existant dans la base")
        print("    2. Afficher la liste des joueurs participant au tournoi")
        print("    3. Sélectionner des joueurs")
        print("    4. Créer un nouveau joueur et l'ajouter au tournoi")
        print("    5. Démarrer le tournoi")
        print("    6. Revenir au menu des tournois")
        print("    7. Sauvegarder et quitter")

        answers = {}

        while True:
            answers = {"Afficher": "1",
                       "Joueurs": "2",
                       "Selectionner": "3",
                       "Creer": "4",
                       "Demmarer": "5",
                       "Revenir": "6",
                       "Sauvegarder": "7"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values() and answer != answers["Afficher"] and answer != answers["Joueurs"]:
                for key, item in answers.items():
                    if item == answer:
                        return key

            if answer in answers.values() and answer == answers["Afficher"]:
                print("----------------------------------------")
                if len(database_players) == 0:
                    print("Il n'y a pas de joueurs dans la base")
                else:
                    print("Voici la liste des joueurs existant dans la base:")

                    for player in database_players:
                        print(player)

                for key, item in answers.items():
                    if item == answer:
                        return key

                return key
            if answer in answers.values() and answer == answers["Joueurs"]:
                self.show_players(players_in_turnament)

                for key, item in answers.items():
                    if item == answer:
                        return key
            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")

    def show_menu_players(self, database_players):
        """Affiche le menu des joueurs"""
        print("----------------------------------------")
        print("Menu des joueurs:")
        print("    1. Afficher la liste des joueurs existant dans la base")
        print("    2. Ajouter un nouveau joueur dans la base")
        print("    3. Revenir au menu principal")
        print("    4. Sauvegarder et quitter")
        answers = {}

        while True:
            answers = {"Afficher": "1",
                       "Ajouter": "2",
                       "Revenir": "3",
                       "Quitter": "4"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values() and answer != answers["Afficher"]:
                for key, item in answers.items():
                    if item == answer:
                        return key

            if answer in answers.values() and answer == answers["Afficher"]:
                print("----------------------------------------")

                if len(database_players) == 0:
                    print("Il n'y a pas de joueurs dans la base")
                else:
                    print("Voici la liste des joueurs existant dans la base:")
                    for player in database_players:
                        print(f"    {player}")

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

    def select_player_from_database(self, database_players, player_name_in_turnament):
        """Selectionne un joueur dans la db et verifie s'il ne participe pas déja dans ce tournois"""
        while True:
            print("----------------------------------------")
            players_to_return = []

            if len(database_players) == 0:
                print("Il n'y a pas de joueurs dans la base")
            else:
                print("Voici la liste des joueurs existant dans la base:")

                for player in database_players:
                    print(f"    {player}")

                database_players_lower = database_players[:]
                for i in range(len(database_players_lower)):
                    database_players_lower[i] = database_players_lower[i].lower()

                player_name_in_turnament_lower = player_name_in_turnament[:]
                for i in range(len(player_name_in_turnament_lower)):
                    player_name_in_turnament_lower[i] = player_name_in_turnament_lower[i].lower()

                print("----------------------------------------")
                players_selected_id = input("Vous pouvez sélectionner des joueurs par leurs identifiants "
                                            "(p1, p2, etc.) ou sélectionner tous les joueurs en "
                                            "écrivant \"all\": ").strip()

                if players_selected_id == "all":
                    players_selected_id_splitted = []
                    for player in database_players:
                        player_splitted = player.split()
                        players_selected_id_splitted.append(player_splitted[2])
                else:
                    players_selected_id = re.sub(r"\s+", "", players_selected_id)
                    players_selected_id_splitted = players_selected_id.split(",")

                for player_selected_id_splitted in players_selected_id_splitted:
                    flag_test_player_existance = False
                    for player in database_players:
                        player_split = player.split()
                        if player_split[2] == player_selected_id_splitted:
                            player_selected = player
                            flag_test_player_existance = True

                            if player_selected.lower() in database_players_lower:
                                if player_selected.lower() in player_name_in_turnament_lower:
                                    print("----------------------------------------")
                                    print(f"Le joueur {player_selected} participe déja à ce tournois")
                                else:
                                    players_to_return.append(player_selected)
                                    print("----------------------------------------")
                                    print(f"Le joueur {player_selected} est ajouté au tournois")
                            else:
                                print("----------------------------------------")
                                print(f"Le joueur avec identifiant p{player_selected_id_splitted} "
                                      "n'existe pas dans la base des joueurs")

                    if flag_test_player_existance is False:
                        print("----------------------------------------")
                        print(f"Le joueur avec identifiant p{player_selected_id_splitted} "
                              "n'existe pas dans la base des joueurs")

            return players_to_return

    def add_one_more_player(self):
        print("----------------------------------------")
        print("Voulez-vous selectionner un autre joueur?")
        print("----------------------------------------")
        print("    1. Oui")
        print("    2. Non")

        answers = {"Oui": "1",
                   "Non": "2"}

        while True:
            answer = input("Votre choix: ").strip()
            if answer in answers.values() and answer == answers["Oui"]:
                for key, item in answers.items():
                    if item == answer:
                        return key

            elif answer in answers.values() and answer == answers["Non"]:
                print("----------------------------------------")
                print("Retour au menu des joueurs")
                for key, item in answers.items():
                    if item == answer:
                        return key
            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")

    def add_one_more__new_player(self):
        print("----------------------------------------")
        print("Voulez-vous ajouter un autre joueur?")
        print("----------------------------------------")
        print("    1. Oui")
        print("    2. Non")

        answers = {"Oui": "1",
                   "Non": "2"}

        while True:
            answer = input("Votre choix: ").strip()
            if answer in answers.values() and answer == answers["Oui"]:
                for key, item in answers.items():
                    if item == answer:
                        return key

            elif answer in answers.values() and answer == answers["Non"]:
                print("----------------------------------------")
                print("Retour au menu des joueurs")
                for key, item in answers.items():
                    if item == answer:
                        return key
            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")
