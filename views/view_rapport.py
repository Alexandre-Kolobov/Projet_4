

class View_rapport():
    def show_menu_rapports(self, database_tournois, database_players, tournois_info_dict):
            print("----------------------------------------")
            print("Menu des rapports:")
            print("    1. Afficher la liste des tournois existant dans la base")
            print("    2. Afficher la liste des joueurs existant dans la base")
            print("    3. Afficher les informations detaillées d'un tournois")
            print("    4. Revenir au menu des tournois")
            print("    5. Quitter le logiciel")
            answers = {}

            while True:
                answers = {"Tournois":"1" ,
                        "Joueurs":"2",
                        "Details":"3",
                        "Revenir":"4",
                        "Quitter":"5"}
                print("----------------------------------------")
                answer = input("Votre choix: ").strip()
                if answer in answers.values() and answer != answers["Tournois"] and answer != answers["Joueurs"]:
                    for key, item in answers.items():
                        if item == answer:
                            return key
                
                if answer in answers.values() and answer == answers["Tournois"]:
                    print("----------------------------------------")
                    print("Voici la list des tournois existants dans la base:")

                    for tournois in database_tournois:
                        # print(f"Tournoi: {tournois_info_dict[tournois]["name"]}")
                        self.show_tournament_informations(tournois_info_dict, tournois)

                    for key, item in answers.items():
                        if item == answer:
                            return key

                    return key

                if answer in answers.values() and answer == answers["Joueurs"]:
                    print("----------------------------------------")
                    print("Voici la list des joueurs existants dans la base:")
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
        print("Voici la list des tournois existants dans la base:")

        for tournois in database_tournois:
            self.show_tournament_informations(tournois_info_dict, tournois)
        print("----------------------------------------")
        tournois_selected = input("Merci de selectionner un tournois: ").strip()
        for i in range(len(database_tournois)):
            database_tournois[i] = database_tournois[i].lower()

        if tournois_selected.lower() in database_tournois:
            print("----------------------------------------")
            print(f"Vous avez selectionné le tournois {tournois_selected}")
            return tournois_selected
        else:
            print("----------------------------------------")
            print(f"Le tournois {tournois_selected} n'existe pas dans la base")
            print("Voulez vous selectionner un autre tournois?")
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
        print("Que voulez vous faire?")
        print("    1. Afficher les joueurs participants")
        print("    2. Afficher les matchs joués")
        print("    3. Revenir au menu des rapports")
        print("    4. Quitter le logiciel")
        answers = {}

        while True:
            answers = {"Joueurs":"1" ,
                    "Matchs":"2",
                    "Revenir":"3",
                    "Quitter":"4"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values() and answer == answers["Joueurs"]:
                print("----------------------------------------")
                print("Voici la liste des joeurs participants au tournoi:")

                tournois_info_dict[select_tournament]['players_list'].sort(key=lambda d: d['first_name'])
                for player in tournois_info_dict[select_tournament]['players_list']:
                    print(f"    {player['first_name']} {player['family_name']} id{player['counter']}")

                for key, item in answers.items():
                    if item == answer:
                        return key
                
            
            if answer in answers.values() and answer == answers["Matchs"]:
                self.show_tournament_informations(tournois_info_dict, select_tournament)
                print("----------------------------------------")
                print("Voici la liste des matchs du tournoi:")
                for round in tournois_info_dict[select_tournament]['round_list']:
                    if len(round['matchs']) != 0:
                        print(f"        Round {round['name'][6:]} :")
                        for match in round['matchs']:
                            player_1_name = match['player_1']['first_name'] + " " + match['player_1']['family_name'] + " " + "id" + str(match['player_1']['counter'])
                            player_2_name = match['player_2']['first_name'] + " " + match['player_2']['family_name'] + " " + "id" + str(match['player_2']['counter'])
                            player_1_score = match['score_1']
                            player_2_score = match['score_2']

                            if player_1_score == 0 and player_2_score ==0:
                                pass
                            else:
                                print(f"            Match: {player_1_name} vs {player_2_name} ---- Score {player_1_score}:{player_2_score}")

                for key, item in answers.items():
                    if item == answer:
                        return key
                    
            if answer in answers.values():
                for key, item in answers.items():
                    if item == answer:
                        return key

    def show_tournament_informations(self, tournois_info_dict, select_tournament):
        if tournois_info_dict[select_tournament]['date_finish'] =="":
            if tournois_info_dict[select_tournament]['round_current'] == 0: 
                print(f"    {tournois_info_dict[select_tournament]['name']} de {tournois_info_dict[select_tournament]['round_all']} rounds ---- Statut - En cours ---- Date du début - {tournois_info_dict[select_tournament]['date_start']} ---- Round en cours - non commencé")
            else:
                print(f"    {tournois_info_dict[select_tournament]['name']} de {tournois_info_dict[select_tournament]['round_all']} rounds ---- Statut - En cours ---- Date du début - {tournois_info_dict[select_tournament]['date_start']} ---- Round en cours - Round {tournois_info_dict[select_tournament]['round_current']}")
        else:
            print(f"    {tournois_info_dict[select_tournament]['name']} de {tournois_info_dict[select_tournament]['round_all']} rounds ---- Statut - Términé ---- Date du début - {tournois_info_dict[select_tournament]['date_start']} ---- Date de fin - {tournois_info_dict[select_tournament]['date_finish']}")
