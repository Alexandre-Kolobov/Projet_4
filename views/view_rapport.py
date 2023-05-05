"""View rapport"""


class View_rapport():
    def show_menu_rapports(self, database_tournois, database_players, tournois_info_dict):
        print("----------------------------------------")
        print("Menu des rapports:")
        print("    1. Afficher la liste des tournois existant dans la base")
        print("    2. Afficher la liste des joueurs existant dans la base")
        print("    3. Afficher les informations détaillées d'un tournoi")
        print("    4. Revenir au menu principal")
        print("    5. Quitter le logiciel")
        answers = {}

        while True:
            answers = {"Tournois": "1",
                       "Joueurs": "2",
                       "Details": "3",
                       "Revenir": "4",
                       "Quitter": "5"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values() and answer != answers["Tournois"] and answer != answers["Joueurs"]:
                for key, item in answers.items():
                    if item == answer:
                        return key

            if answer in answers.values() and answer == answers["Tournois"]:
                print("----------------------------------------")
                if len(database_tournois) == 0:
                    print("Il n'y a pas de tournoi dans la base")
                else:
                    print("Voici la liste des tournois existant dans la base:")
                for tournois in database_tournois:
                    self.show_tournament_informations(tournois_info_dict, tournois)

                for key, item in answers.items():
                    if item == answer:
                        return key

                return key

            if answer in answers.values() and answer == answers["Joueurs"]:
                print("----------------------------------------")
                if len(database_players) == 0:
                    print("Il n'y a pas de joueur dans la base")
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

    def select_tournament(self, database_tournois, tournois_info_dict):
        print("----------------------------------------")
        if len(database_tournois) == 0:
            print("Il n'y a pas de tournoi dans la base")
            print("Retour au menu des rapports")
            return None
        else:
            print("Voici la liste des tournois existant dans la base:")

        for tournois in database_tournois:
            self.show_tournament_informations(tournois_info_dict, tournois)
        print("----------------------------------------")
        while True:
            tournois_selected = input("Merci de selectionner un tournois: ").strip()

            if tournois_selected in database_tournois:
                print("----------------------------------------")
                print(f"Vous avez selectionné le tournois {tournois_selected}")
                return tournois_selected
            else:
                print("----------------------------------------")
                print(f"Le tournois {tournois_selected} n'existe pas dans la base")
                print("Voulez-vous selectionner un autre tournois?")
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

    def show_menu_details(self, tournois_info_dict, select_tournament):
        print("----------------------------------------")
        print("Que voulez-vous faire?")
        print("    1. Afficher les joueurs participants")
        print("    2. Afficher les matchs joués")
        print("    3. Revenir au menu des rapports")
        print("    4. Quitter le logiciel")
        answers = {}

        while True:
            answers = {"Joueurs": "1",
                       "Matchs": "2",
                       "Revenir": "3",
                       "Quitter": "4"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values() and answer == answers["Joueurs"]:
                print("----------------------------------------")
                tournois_info_dict[select_tournament]['players_list'].sort(key=lambda d: d['first_name'])

                if len(tournois_info_dict[select_tournament]['players_list']) == 0:
                    print("Il n'y a pas de joueurs participant à ce tournoi")
                else:
                    print("Voici la liste des joueurs participant:")
                    for player in tournois_info_dict[select_tournament]['players_list']:
                        print(f"    {player['first_name']} {player['family_name']} p{player['counter']}")

                for key, item in answers.items():
                    if item == answer:
                        return key

            if answer in answers.values() and answer == answers["Matchs"]:
                self.show_tournament_informations(tournois_info_dict, select_tournament)
                print("----------------------------------------")
                if len(tournois_info_dict[select_tournament]['round_list']) == 0:
                    print("Il n'y a pas eu de matchs pour ce tournoi")
                else:
                    print("Voici la liste des matchs du tournoi:")
                    for round in tournois_info_dict[select_tournament]['round_list']:
                        if len(round['matchs']) != 0:
                            print(f"        Round {round['name'][6:]} :")
                            for match in round['matchs']:
                                p1_first_name = match['player_1']['first_name']
                                p1_family_name = match['player_1']['family_name']
                                p1_id = "p" + str(match['player_1']['counter'])

                                p2_first_name = match['player_2']['first_name']
                                p2_family_name = match['player_2']['family_name']
                                p2_id = "p" + str(match['player_2']['counter'])

                                player_1_name = p1_first_name + " " + p1_family_name + " " + p1_id
                                player_2_name = p2_first_name + " " + p2_family_name + " " + p2_id
                                player_1_score = match['score_1']
                                player_2_score = match['score_2']

                                if player_1_score == 0 and player_2_score == 0:
                                    pass
                                else:
                                    print(f"            Match: {player_1_name} vs {player_2_name} ---- "
                                          f"Score {player_1_score}:{player_2_score}")

                for key, item in answers.items():
                    if item == answer:
                        return key

            if answer in answers.values():
                for key, item in answers.items():
                    if item == answer:
                        return key

    def show_tournament_informations(self, tournois_info_dict, select_tournament):
        if tournois_info_dict[select_tournament]['date_finish'] == "":
            if tournois_info_dict[select_tournament]['round_current'] == 0:
                print(f"Tournoi - {tournois_info_dict[select_tournament]['name']}")
                print(f"    Nombre de rounds: {tournois_info_dict[select_tournament]['round_all']}")
                print(f"    Participants {tournois_info_dict[select_tournament]['nomber_tournament_players']} "
                      f"/ {tournois_info_dict[select_tournament]['tournament_min_players']} (min nécessaire)")
                print("    Statut - En préparation")
                print(f"    Date du début - {tournois_info_dict[select_tournament]['date_start_schedule']}")
                print(f"    Date de fin - {tournois_info_dict[select_tournament]['date_finish_schedule']}")
                print("    Round en cours - non commencé")
            else:
                print(f"Tournoi - {tournois_info_dict[select_tournament]['name']}")
                print(f"    Nombre de rounds: {tournois_info_dict[select_tournament]['round_all']}")
                print(f"    Participants {tournois_info_dict[select_tournament]['nomber_tournament_players']} "
                      f"/ {tournois_info_dict[select_tournament]['tournament_min_players']} (min nécessaire)")
                print("    Statut - En cours")
                print(f"    Date du début - {tournois_info_dict[select_tournament]['date_start']}")
                print(f"    Date de fin - {tournois_info_dict[select_tournament]['date_finish_schedule']}")
                print(f"    Round en cours - Round {tournois_info_dict[select_tournament]['round_current']}")
        else:
            print(f"Tournoi - {tournois_info_dict[select_tournament]['name']}")
            print(f"    Nombre de rounds: {tournois_info_dict[select_tournament]['round_all']}")
            print(f"    Participants {tournois_info_dict[select_tournament]['nomber_tournament_players']} "
                  f"/ {tournois_info_dict[select_tournament]['tournament_min_players']} (min nécessaire)")
            print("    Statut - Terminé")
            print(f"    Date du début - {tournois_info_dict[select_tournament]['date_start']}")
            print(f"    Date de fin - {tournois_info_dict[select_tournament]['date_finish']}")
            print("    Round en cours - Terminé")
