"""View match"""


class View_match():
    def play_match(self, player_1_name, player_2_name):
        print("----------------------------------------")
        print(f"Match {player_1_name} contre {player_2_name}")

        while True:
            match_result = input("Entrer nom et prenom du gagnat ou \"égalité\": ").strip()

            if match_result in [player_1_name, player_2_name, "égalité"]:
                break
            else:
                print("Le resultat n'a pas été entré correctemment. Merci de reesayer.")

        return match_result

    def show_match_result(self, player_1_name, player_2_name, player_1_score, player_2_score):
        print(f"    Match: {player_1_name} vs {player_2_name} ---- Score {player_1_score}:{player_2_score}")
        
    def played_match(player_1_name, player_2_name, player_1_score, player_2_score):

        print(
            f"Ce match ([{player_1_name},{player_1_score}], [{player_2_name},{player_2_score}]) "
            "a déjà été joué lors de précédent lancement du logiciel."
            )

    def get_finish_match(self):
            print("----------------------------------------")
            print(f"Voulez vous jouer le match suivant?")
            print("    1. Oui")
            print("    2. Sauvegarder et revenir au menu des tournois")
            print("    3. Sauvegarder et quitter")
                                        
            answers = {}

            while True:
                answers = {"Oui":"1" ,
                        "Revenir":"2",
                        "Quitter":"3"}
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