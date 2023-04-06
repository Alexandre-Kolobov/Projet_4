class Player:
    def __init__ (self, first_name, family_name, birth_date, score = 0, random_number = 0, ingame = False):
        self.first_name = first_name
        self.family_name = family_name
        self.birth_date = birth_date
        self.score = score
        self.random_number = random_number
        self.ingame = ingame
        self.played_with = []

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

    def give_player_score(self):
        return self.score
    
    def update_ingame_status(self, ingame):
        self.ingame = ingame

    def give_ingame_status(self):
        return self.ingame

    def add_played_with(self, player):
        self.played_with.append(player)

    def check_played_with(self, player):
        if player in self.played_with:
            return True
        else:
            return False