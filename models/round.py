from datetime import datetime
match_counter = 0


class Round:
    def __init__(self, name, date_start="", date_finish="", finish_status=False):
        self.name = name
        self.matchs = []
        self.date_start = date_start
        self.date_finish = date_finish
        self.finish_status = finish_status

    def __repr__(self):
        return f"{self.name[6:]}"

    def add_match(self, match):
        self.matchs.append(match)

    def give_match_list(self):
        return self.matchs

    def give_round_name(self):
        return self.name

    def give_finish_status(self):
        return self.finish_status

    def update_finish_status(self, finish_status):
        self.finish_status = finish_status
        round_date_finish = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.date_finish = round_date_finish

    def start_round(self):
        round_date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.date_start = round_date_start
