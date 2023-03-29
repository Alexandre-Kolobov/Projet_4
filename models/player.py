class Player:
    def __init__ (self, first_name, family_name, birth_date, score = 0):
        self.first_name = first_name
        self.family_name = family_name
        self.birth_date = birth_date
        self.score = score
        #Penser à verifier les inputs client

    def __repr__(self):
        return(f"{self.first_name} {self.family_name}")

    def save_players_json(self):
        pass