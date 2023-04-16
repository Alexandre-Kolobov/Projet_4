"""View tournament"""


class View_tournament():
    def show_menu_tournament(self, database_tournois):
        print("----------------------------------------")
        print("Menu du tournois:")
        print("    1. Afficher la liste des tournois existants dans la base")
        print("    2. Sélectionner un tournois dans la base des tournois")
        print("    3. Créer un nouveau tournois")
        answers = {}

        while True:
            answers = {"Afficher":"1" ,
                       "Selectionner":"2",
                       "Creer":"3"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values() and answer != answers["Afficher"]:
                for key, item in answers.items():
                    if item == answer:
                        return key
            
            elif answer in answers.values() and answer == answers["Afficher"]:
                print("----------------------------------------")
                print("Voici la list des tournois existants dans la base:")

                for tournois in database_tournois:
                    print(tournois)

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
                    
            answer = input("Votre choix: ").strip()
            while True:
                if answer in answers.values() and answer == answers["Oui"]:
                    
                        round_all = input("Combien de round voulez vous jouer?")

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


    def select_tournament_from_database(self, database_tournois):
        """Selectionne un tournois dans la db"""
        database_to_print = database_tournois[:]
        while True:
            print("----------------------------------------")
            print("Voici la list des tournois existants dans la base:")

            for tournois in database_to_print:
                print(tournois)

            print("----------------------------------------")
            tournois_selected = input("Merci de selectionner un tournois: ").strip()
            for i in range(len(database_tournois)):
                database_tournois[i] = database_tournois[i].lower()

            if tournois_selected.lower() in database_tournois:
                print("----------------------------------------")
                print(f"Vous avez slectionné le tournois {tournois_selected}")
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
            print(f"Place {place}: {player} - score {score}")
        else:
            print(f"Place {place}: {player} - score {score}")


    def show_players(self, players):
        print("----------------------------------------")
        print("Voici la liste des joueurs participants:")
        for i in players:
            print(i)

    def show_player_score(self, player, score):
        print (f"{player} - {score}")
