data_path = "data\\tournaments\\"


class Player:
    def __init__(self, first_name, family_name, birth_date):
        self.first_name = first_name
        self.family_name = family_name
        self.birth_date = birth_date

    def __repr__(self):
        return (f"{self.first_name} {self.family_name}")

    def give_player_name(self):
        return (f"{self.first_name} {self.family_name}")
