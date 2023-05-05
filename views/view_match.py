"""View match"""


class View_match():
    def play_match(self, player_1_name, player_2_name):
        """Input pour le resultat d'un match"""

        print("----------------------------------------")
        print(f"Match {player_1_name} contre {player_2_name}")

        while True:
            player_1_name_splited = player_1_name.split()
            player_1_id = player_1_name_splited[2]

            player_2_name_splited = player_2_name.split()
            player_2_id = player_2_name_splited[2]
            match_result = input("Entrer l'identifiant du gagnant ou \"égalité\": ").strip()

            if match_result in [player_1_id, player_2_id, "égalité"]:
                break
            else:
                print("Le resultat n'a pas été entré correctemment. Merci de reesayer.")

        if match_result == player_1_id:
            return player_1_name

        if match_result == player_2_id:
            return player_2_name

        if match_result == "égalité":
            return match_result

    def show_match_result(self, player_1_name, player_2_name, player_1_score, player_2_score):
        """Affiche le resultat d'un match"""
        print(f"    Match: {player_1_name} vs {player_2_name} ---- Score {player_1_score}:{player_2_score}")

    def get_finish_match(self):
        """Affiche les actions à proposer à la fin d'un match"""
        print("----------------------------------------")
        print("Voulez-vous jouer le match suivant?")
        print("    1. Oui")
        print("    2. Sauvegarder et revenir au menu des tournois")
        print("    3. Sauvegarder et quitter")

        answers = {}

        while True:
            answers = {"Oui": "1",
                       "Revenir": "2",
                       "Quitter": "3"}
            print("----------------------------------------")
            answer = input("Votre choix: ").strip()
            if answer in answers.values():
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
