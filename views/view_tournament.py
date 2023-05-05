"""View tournament"""
from datetime import datetime
import time

class View_tournament():
    def show_main_manu(self):
        """Affiche menu du logiciel"""
        print("----------------------------------------")
        print("Menu:")
        print("    1. Rapports")
        print("    2. Joueurs")
        print("    3. Tournois")
        print("    4. Quitter le logiciel")
        answers = {}

        while True:
            answers = {"Rapports": "1",
                       "Joueurs": "2",
                       "Tournois": "3",
                       "Quitter": "4"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values():
                for key, item in answers.items():
                    if item == answer:
                        return key

            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")

    def show_tournament_menu(self):
        """Affiche menu du logiciel"""
        print("----------------------------------------")
        print("Menu des tournois:")
        print("    1. Reprendre un tournoi dans la base des tournois")
        print("    2. Créer un nouveau tournois")
        print("    3. Revenir au menu principal")
        print("    4. Quitter le logiciel")
        answers = {}

        while True:
            answers = {"Reprendre": "1",
                       "Creer": "2",
                       "Revenir": "3",
                       "Quitter": "4"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values():
                for key, item in answers.items():
                    if item == answer:
                        return key

            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")

    def get_tournament_start_informations(self, round_all, database_tournois):
        """Input des information pour créer un tournoi"""
        while True:
            while True:
                print("----------------------------------------")
                name = input("Entrer le titre du tournoi: ").strip()
                if len(name) >= 1:
                    tournament_name = name

                    if tournament_name in database_tournois:
                        print("----------------------------------------")
                        print(f"Le tournois {tournament_name} existe déja dans la base des tournois")
                        print("Que voulez-vous faire?")
                        print("    1. Réessayer le saisie")
                        print("    2. Revenir dans le menu des tournois")

                        answers = {"Reessayer": "1",
                                   "Revenir": "2"}

                        answer = input("Votre choix: ").strip()

                        if answer in answers.values() and answer == answers["Reessayer"]:
                            pass

                        elif answer in answers.values() and answer == answers["Revenir"]:
                            print("----------------------------------------")
                            print("Retour au menu des tournois")
                            return None
                    else:
                        break
                else:
                    print("Le titre du tournoi ne dois pas être vide. Merci de le reinsegner.")

            while True:
                print("----------------------------------------")
                place = input(f"Entrer l'endroit du tournoi {name}: ").strip()
                if len(place) >= 1:
                    break
                else:
                    print("L'endroit du tournoi ne dois pas être vide. Merci de le reinsegner.")

            while True:
                print("----------------------------------------")
                date_start_schedule = input(f"Entrer la date et l'heure du début du tournoi {name} (DD/MM/YYYY HH:MM): ").strip()
                date_start_schedule = date_start_schedule + ":00"
                try:
                    datetime.strptime(date_start_schedule, "%d/%m/%Y %H:%M:%S")
                    break
                except (ValueError, TypeError):
                    print("La date de début du tournoi doit être au format DD/MM/YYYY HH:MM")

            while True:
                print("----------------------------------------")
                date_finish_schedule = input(f"Entrer la date et l'heure de la fin du tournoi {name} (DD/MM/YYYY HH:MM): ").strip()
                date_finish_schedule = date_finish_schedule + ":00"
                try:
                    datetime.strptime(date_finish_schedule, "%d/%m/%Y %H:%M:%S")
                    first = datetime.strptime(date_start_schedule, "%d/%m/%Y %H:%M:%S")
                    second = datetime.strptime(date_finish_schedule, "%d/%m/%Y %H:%M:%S")
                    if first >= second:
                        print("La date de début du tournoi ne doit pas être superieur ou égale à la date de fin")
                    else:
                        break

                except (ValueError, TypeError):
                    print("La date de début du tournoi doit être au format DD/MM/YYYY HH:MM")

            print("----------------------------------------")
            description = input(f"Entrer la description du tournoi {name}: ").strip()

            print("----------------------------------------")
            print(f"Le nombre des rounds prédéfini est {round_all}")
            print("Voulez-vous modifier ce paramètre?")
            print("    1. Oui")
            print("    2. Non")

            answers = {"Oui": "1",
                       "Non": "2"}

            while True:
                answer = input("Votre choix: ").strip()
                if answer in answers.values() and answer == answers["Oui"]:
                    print("----------------------------------------")
                    print("Combien de round voulez-vous jouer?")
                    round_all = input("Nombre des rounds: ")
                    try:
                        int(round_all)
                        break
                    except ValueError:
                        print("Merci d'entrer un nombre des rounds.")

                elif answer in answers.values() and answer == answers["Non"]:
                    break

                else:
                    answers_list = []
                    for i in answers.values():
                        answers_list.append(i)
                    answers_list.sort()
                    print(f"Merci de reesayer en choissisant parmis {answers_list}")

            break

        return name, place, description, round_all, date_start_schedule, date_finish_schedule

    def select_tournament_from_database(self, database_tournois, tournois_info_dict):
        """Selectionne un tournois dans la db"""
        while True:
            print("----------------------------------------")
            print("Voici la liste des tournois existant non terminé dans la base:")

            for tournois in database_tournois:
                if tournois_info_dict[tournois]['date_finish'] == "":
                    if tournois_info_dict[tournois]['round_current'] == 0:
                        print(f"Tournoi - {tournois_info_dict[tournois]['name']}")
                        print(f"    Nombre de rounds: {tournois_info_dict[tournois]['round_all']}")
                        print(f"    Participants {tournois_info_dict[tournois]['nomber_tournament_players']} / {tournois_info_dict[tournois]['tournament_min_players']} (min nécessaire)")
                        print(f"    Statut - En préparation")
                        print(f"    Date du début - {tournois_info_dict[tournois]['date_start_schedule']}")
                        print(f"    Date de fin - {tournois_info_dict[tournois]['date_finish_schedule']}")
                        print("    Round en cours - non commencé")
                    else:
                        print(f"Tournoi - {tournois_info_dict[tournois]['name']}")
                        print(f"    Nombre de rounds: {tournois_info_dict[tournois]['round_all']}")
                        print(f"    Participants {tournois_info_dict[tournois]['nomber_tournament_players']} / {tournois_info_dict[tournois]['tournament_min_players']} (min nécessaire)")
                        print(f"    Statut - En cours")
                        print(f"    Date du début - {tournois_info_dict[tournois]['date_start']}")
                        print(f"    Date de fin - {tournois_info_dict[tournois]['date_finish_schedule']}")
                        print(f"    Round en cours - Round {tournois_info_dict[tournois]['round_current']}")
                else:
                    pass
                    # print(f"Tournoi - {tournois_info_dict[tournois]['name']}")
                    # print(f"    Nombre de rounds: {tournois_info_dict[tournois]['round_all']}")
                    # print(f"    Participants {tournois_info_dict[tournois]['nomber_tournament_players']} / {tournois_info_dict[tournois]['tournament_min_players']} (min nécessaire)")
                    # print(f"    Statut - Terminé")
                    # print(f"    Date du début - {tournois_info_dict[tournois]['date_start']}")
                    # print(f"    Date de fin - {tournois_info_dict[tournois]['date_finish']}")
                    # print("    Round en cours - Terminé")

            print("----------------------------------------")
            tournois_selected = input("Merci de selectionner un tournois: ").strip()

            if tournois_selected in database_tournois and tournois_info_dict[tournois_selected]['date_finish'] == "":
                print("----------------------------------------")
                print(f"Vous avez selectionné le tournois {tournois_selected}")
                return tournois_selected
            else:            
                if tournois_selected in database_tournois and tournois_info_dict[tournois_selected]['date_finish'] != "":
                    print("----------------------------------------")
                    print(f"Il n'est pas possible de sélectionner un tournoi finit {tournois_selected}.")
                    print(f"Si vous souhaitez consulter ses informations, veuillez utiliser le menu \"Rapports\".")
                else:
                    print("----------------------------------------")
                    print(f"Le tournois {tournois_selected} n'existe pas dans la base")

                print("Voulez-vous sélectionner un autre tournois?")
                print("----------------------------------------")
                print("    1. Oui")
                print("    2. Non")

                answers = {"Oui": "1",
                        "Non": "2"}

                answer = input("Votre choix: ").strip()
                if answer in answers.values() and answer == answers["Oui"]:
                    pass

                elif answer in answers.values() and answer == answers["Non"]:
                    print("----------------------------------------")
                    print("Retour au menu des tournois")
                    return None
                else:
                    answers_list = []
                    for i in answers.values():
                        answers_list.append(i)
                    answers_list.sort()
                    print(f"Merci de reesayer en choissisant parmis {answers_list}")

    def show_classment(self, player, place, score):
        """Affiche le classment"""
        if place == 1:
            print("Voici le classement du tournoi:")
            print(f"    Place {place}: {player} - score {score}")
        else:
            print(f"    Place {place}: {player} - score {score}")

    def show_players(self, players):
        """Affiche les joueurs"""
        print("----------------------------------------")
        print("Voici la liste des joueurs participant:")
        for i in players:
            print(f"    {i}")

    def show_welcome(self):
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print(r"                                                  _:_    ")
        print(r"                                                 '-.-'   ")
        print(r"                                        ()      __.'.__  ")
        print(r"                                     .-:--:-.  |_______| ")
        print(r"                              ()      \____/    \=====/  ")
        print(r"                              /\      {====}     )___(   ")
        print(r"                   (\=,      /  \      )__(     /_____\  ")
        print(r"   __    |'-'-'|  //  .\    (    )    /____\     |   |   ")
        print(r"  /  \   |_____| (( \_  \    )__(      |  |      |   |   ")
        print(r"  \__/    |===|   ))  `\_)  /____\     |  |      |   |   ")
        print(r" /____\   |   |  (/     \    |  |      |  |      |   |   ")
        print(r"  |  |    |   |   | _.-'|    |  |      |  |      |   |   ")
        print(r"  |__|    )___(    )___(    /____\    /____\    /_____\  ")
        print(r" (====)  (=====)  (=====)  (======)  (======)  (=======) ")
        print(r" }===={  }====={  }====={  }======{  }======{  }======={ ")
        print(r"(______)(_______)(_______)(________)(________)(_________)")

    def tournament_status(self,
                          tournament_name,
                          tournament_start,
                          tournament_finish,
                          tournament_round_current,
                          tournament_round_all,
                          tournament_start_shedule,
                          tournament_finish_shedule,
                          tournament_players,
                          tournament_min_players):
        """Affiche le statut d'un tournois en temps réel"""
        print("----------------------------------------")
        if tournament_finish == "":
            if tournament_round_current == 0:
                print(f"Tournoi - {tournament_name}")
                print(f"    Nombre de rounds: {tournament_round_all}")
                print(f"    Participants {tournament_players} / {tournament_min_players} (min nécessaire)")
                print(f"    Statut - En préparation")
                print(f"    Date du début - {tournament_start_shedule}")
                print(f"    Date de fin - {tournament_finish_shedule}")
                print("    Round en cours - non commencé")
            else:
                print(f"Tournoi - {tournament_name}")
                print(f"    Nombre de rounds: {tournament_round_all}")
                print(f"    Participants {tournament_players} / {tournament_min_players} (min nécessaire)")
                print(f"    Statut - En cours")
                print(f"    Date du début - {tournament_start}")
                print(f"    Date de fin - {tournament_finish_shedule}")
                print(f"    Round en cours - Round {tournament_round_current}")
        else:
                print(f"Tournoi - {tournament_name}")
                print(f"    Nombre de rounds: {tournament_round_all}")
                print(f"    Participants {tournament_players} / {tournament_min_players} (min nécessaire)")
                print(f"    Statut - Terminé")
                print(f"    Date du début - {tournament_start}")
                print(f"    Date de fin - {tournament_finish}")
                print("    Round en cours - Terminé")

    def show_menu_post_tournament(self):
        """Affiche les actions à faire àpres le tournois"""
        print("----------------------------------------")
        print("Que voulez-vous faire:")
        print("    1. Afficher les joueurs participant au tournoi")
        print("    2. Afficher les matchs")
        print("    3. Revenir au menu principal")
        print("    4. Quitter le logiciel")
        answers = {}

        while True:
            answers = {"Joueurs": "1",
                       "Matchs": "2",
                       "Revenir": "3",
                       "Quitter": "4"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values():
                for key, item in answers.items():
                    if item == answer:
                        return key

            if answer in answers.values() and answer == answers["Afficher"]:
                print("----------------------------------------")
                print("Voici la liste des tournois existant dans la base:")

            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")
