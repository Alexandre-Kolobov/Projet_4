class Player:
    def __init__ (self, first_name, family_name, birth_date, score = 0, random_number = 0):
        self.first_name = first_name
        self.family_name = family_name
        self.birth_date = birth_date
        self.score = score
        self.random_number = random_number
        #Penser à verifier les inputs client

    def __repr__(self):
        return(f"{self.first_name} {self.family_name}")

    def save_players_json(self):
        pass

    def add_random_number(self, random_number):
        self.random_number = random_number

    def give_player_name(self):
        return(f"{self.first_name} {self.family_name}")
    
    def update_player_score(self, score):
        self.score += int(score)