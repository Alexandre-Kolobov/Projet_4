"""View match"""


class View_match():
    def play_match(self, player_1_name, player_2_name):
        print("\n")
        print(f"{player_1_name} et {player_2_name} jouent.")

        while True:
            match_result = input("Entrer nom et prenom du gagnat ou \"égalité\": ").strip()

            if match_result in [player_1_name, player_2_name, "égalité"]:
                break
            else:
                print("Le resultat n'a pas été entré correctemment. Merci de reesayer.")

        return match_result

    def played_match(
            player_1_name, player_2_name, player_1_score, player_2_score):

        print(
            f"Ce match ([{player_1_name},{player_1_score}], [{player_2_name},{player_2_score}]) "
            "a déjà été joué lors de précédent lancement du logiciel."
            )
