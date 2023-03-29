class Round: # pas d'heritage
    def __init__(self, name, date_start = "", date_finish = ""):
        self.name = name
        self.matchs = []
        self.date_start = date_start
        self.date_finish = date_finish

    def __repr__(self):
        return f"{self.name}"
    
    def add_match(self):
        pass