class Round:
    def __init__(self, name, date_start = "", date_finish = ""):
        self.name = name
        self.matchs = []
        self.date_start = date_start
        self.date_finish = date_finish

    def __repr__(self):
        return f"{self.name}"
    
    def add_match(self, match):
        self.matchs.append(match)
    
    def give_match_list(self):
        return self.matchs
    
    def give_round_name(self):
        return self.name
    
    def add_date_finish(self, date_finish):
        self.date_finish = date_finish