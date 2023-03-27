class Player:
    def __init__ (self, first_name, family_name, birth_date, score = 0, in_game = False):
        self.first_name = first_name
        self.family_name = family_name
        self.birth_date = birth_date
        self.score = score
        self.already_played_with = []
        self.in_game = in_game
        #Penser à verifier les inputs client

    def __repr__(self):
        # return(f"Prenom: {self.first_name}\nNom: {self.family_name}\nDate de naissance: {self.birth_date}\n")
        return(f"{self.first_name} {self.family_name}")
    # def __str__(self):
    #     return("TEST 2")

    def save_players_json(self):
        pass