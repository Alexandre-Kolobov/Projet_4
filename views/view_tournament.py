"""View tournament"""


class View_tournament():
    def get_tournament_start_informations(self, round_all):
        while True:
            name = input("Entrer le titre du tournoi: ").strip()
            if len(name) >= 1:
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

        round = input(f"Voulez vous changer le nombre de round qui est {round_all} par defaut "
                        "(y/n)?").strip().lower()
        while True:
            if round == "y":
                round_all = input("Combien de round voulez vous jouer?")
                try:
                    int(round_all)
                    break
                except ValueError:
                    print("Merci d'entrer un nombre.")
            elif round =="n":
                break
            else:
                round = input(f"Voulez vous changer le nombre de round qui est {round_all} par defaut "
                                "(y/n)?").strip().lower()

        return name, place, description, round_all

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

    def show_menu_tournament(self, database_tournois):
        print("----------------------------------------")
        print("Menu du tournois:")
        print("    1. Afficher la liste des tournois existants dans la base")
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