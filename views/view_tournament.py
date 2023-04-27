"""View tournament"""


class View_tournament():
    # def show_menu_tournament(self, database_tournois, database_players):
    #     print("----------------------------------------")
    #     print("Menu du tournois:")
    #     print("    1. Afficher la liste des tournois existant dans la base")
    #     print("    2. Afficher la liste des joueurs existant dans la base")
    #     print("    3. Sélectionner un tournois dans la base des tournois")
    #     print("    4. Créer un nouveau tournois")
    #     print("    5. Quitter le logiciel")
    #     answers = {}

    #     while True:
    #         answers = {"Afficher":"1" ,
    #                    "Joueurs":"2",
    #                    "Selectionner":"3",
    #                    "Creer":"4",
    #                    "Quitter":"5"}
    #         print("----------------------------------------")
    #         answer = input("Votre choix: ").strip()
    #         if answer in answers.values() and answer != answers["Afficher"] and answer != answers["Joueurs"]:
    #             for key, item in answers.items():
    #                 if item == answer:
    #                     return key
            
    #         if answer in answers.values() and answer == answers["Afficher"]:
    #             print("----------------------------------------")
    #             print("Voici la list des tournois existants dans la base:")

    #             for tournois in database_tournois:
    #                 print(tournois)

    #             for key, item in answers.items():
    #                 if item == answer:
    #                     return key

    #             return key

    #         if answer in answers.values() and answer == answers["Joueurs"]:
    #             print("----------------------------------------")
    #             print("Voici la list des joueurs existants dans la base:")
    #             for player in database_players:
    #                 print(player)

    #             for key, item in answers.items():
    #                 if item == answer:
    #                     return key

    #             return key

    #         else:
    #             answers_list = []
    #             for i in answers.values():
    #                 answers_list.append(i)
    #             answers_list.sort()
    #             print(f"Merci de reesayer en choissisant parmis {answers_list}")

    def show_menu_tournament(self, database_tournois, database_players):
        print("----------------------------------------")
        print("Menu du tournois:")
        print("    1. Rapports")
        print("    2. Sélectionner un tournois dans la base des tournois")
        print("    3. Créer un nouveau tournois")
        print("    4. Quitter le logiciel")
        answers = {}

        while True:
            answers = {"Rapports":"1" ,
                       "Selectionner":"2",
                       "Creer":"3",
                       "Quitter":"4"}
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
        while True:
            while True:
                name = input("Entrer le titre du tournoi: ").strip()
                if len(name) >= 1:
                    tournament_name = name.lower()
                    for i in range(len(database_tournois)):
                        database_tournois[i] = database_tournois[i].lower()

                    if tournament_name in database_tournois:
                        print("----------------------------------------")
                        print(f"Le tournois {tournament_name} existe déja dans la base des tournois")
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
                            print("Retour au menu de tournois")
                            return None
                    else:
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

            print(f"Le nombre des rounds par defaut est {round_all}")
            print("Voulez vous modifier ce paramètre?")
            print("    1. Oui")
            print("    2. Non")

            answers = {"Oui":"1" ,
                       "Non":"2"}
                    
            
            while True:
                answer = input("Votre choix: ").strip()
                if answer in answers.values() and answer == answers["Oui"]:
                        print("----------------------------------------")
                        print("Combien de round voulez vous jouer?")
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

        return name, place, description, round_all


    def select_tournament_from_database(self, database_tournois, tournois_info_dict):
        """Selectionne un tournois dans la db"""
        # database_to_print = database_tournois[:]
        while True:
            print("----------------------------------------")
            print("Voici la list des tournois existants dans la base:")

            for tournois in database_tournois:
                # print(f"Tournoi: {tournois_info_dict[tournois]["name"]}")
                if tournois_info_dict[tournois]['date_finish'] =="":
                    if tournois_info_dict[tournois]['round_current'] == 0: 
                        print(f"    {tournois_info_dict[tournois]['name']} de {tournois_info_dict[tournois]['round_all']} rounds ---- Statut - En cours ---- Date du début - {tournois_info_dict[tournois]['date_start']} ---- Round en cours - non commencé")
                    else:
                        print(f"    {tournois_info_dict[tournois]['name']} de {tournois_info_dict[tournois]['round_all']} rounds ---- Statut - En cours ---- Date du début - {tournois_info_dict[tournois]['date_start']} ---- Round en cours - Round {tournois_info_dict[tournois]['round_current']}")
                else:
                    print(f"    {tournois_info_dict[tournois]['name']} de {tournois_info_dict[tournois]['round_all']} rounds ---- Statut - Términé ---- Date du début - {tournois_info_dict[tournois]['date_start']} ---- Date de fin - {tournois_info_dict[tournois]['date_finish']}")


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

    def show_classment(self, player, place, score):
        if place == 1:
            print("Voici le classement du tournois:")
            print(f"    Place {place}: {player} - score {score}")
        else:
            print(f"    Place {place}: {player} - score {score}")


    def show_players(self, players):
        print("----------------------------------------")
        print("Voici la liste des joueurs participants:")
        for i in players:
            print(f"    {i}")

    def show_player_score(self, player, score):
        print (f"{player} - {score}")

    def show_welcome(self):
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("                                                  _:_    ")
        print("                                                 '-.-'   ")
        print("                                        ()      __.'.__  ")
        print("                                     .-:--:-.  |_______| ")
        print("                              ()      \____/    \=====/  ")
        print("                              /\      {====}     )___(   ")
        print("                   (\=,      /  \      )__(     /_____\  ")
        print("   __    |'-'-'|  //  .\    (    )    /____\     |   |   ")
        print("  /  \   |_____| (( \_  \    )__(      |  |      |   |   ")
        print("  \__/    |===|   ))  `\_)  /____\     |  |      |   |   ")
        print(" /____\   |   |  (/     \    |  |      |  |      |   |   ")
        print("  |  |    |   |   | _.-'|    |  |      |  |      |   |   ")
        print("  |__|    )___(    )___(    /____\    /____\    /_____\  ")
        print(" (====)  (=====)  (=====)  (======)  (======)  (=======) ")
        print(" }===={  }====={  }====={  }======{  }======{  }======={ ")
        print("(______)(_______)(_______)(________)(________)(_________)")

    def tournament_status(self, tournament_name, tournament_start, tournament_finish, tournament_round_current, tournament_round_all):
        print("----------------------------------------")
        if tournament_finish =="":
            if tournament_round_current == 0: 
                print(f"Tournoi - {tournament_name} de {tournament_round_all} rounds ---- Statut - En cours ---- Date du début - {tournament_start} ---- Round en cours - non commencé")
            else:
                print(f"Tournoi - {tournament_name} ---- Statut - En cours ---- Date du début - {tournament_start} ---- Round en cours - Round {tournament_round_current}")
        else:
            print(f"Tournoi - {tournament_name} ---- Statut - Términé ---- Date du début - {tournament_start} ---- Date de fin - {tournament_finish}")



    def show_menu_post_tournament(self):
        print("----------------------------------------")
        print("Que voulez vous faire:")
        print("    1. Afficher les joeurs participants au tournoi")
        print("    2. Afficher les matchs")
        print("    3. Revenir au menu des tournois")
        print("    4. Quitter le logiciel")
        answers = {}

        while True:
            answers = {"Joueurs":"1" ,
                       "Matchs":"2",
                       "Revenir":"3",
                       "Quitter":"4"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values():
                for key, item in answers.items():
                    if item == answer:
                        return key
            
            if answer in answers.values() and answer == answers["Afficher"]:
                print("----------------------------------------")
                print("Voici la list des tournois existants dans la base:")

            else:
                answers_list = []
                for i in answers.values():
                    answers_list.append(i)
                answers_list.sort()
                print(f"Merci de reesayer en choissisant parmis {answers_list}")