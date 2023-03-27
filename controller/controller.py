class Controller:
    def __init__(self):
        self.players = []
        self.round_dict = {}

    def get_players(self):

        player_informations = View().get_player_informations()

        first_name = player_informations[0]
        family_name = player_informations[1]
        birth_date = player_informations[2]
        add_player = player_informations[3]

        player = Player(first_name, family_name, birth_date)
        self.players.append(player)

        if add_player == "y":
            self.get_players() 

        return self.players
    

    def create_pairs(self):
        

        list_pairs = []
        r = 0

        participants = self.get_players() #["A", "B", "C", "D"]  #self.players
        
        show_players = View().show_players(self.players)

        if (len(participants) % 2) != 0: #pour faire les paires correctemment il nous faut un nombre paire des joueurs
            participants.append("Filler")

        pairs = combinations(participants, 2)
        
        for pair in pairs:
            list_pairs.append(pair)

        while len(list_pairs) > 0:
            i = 0
            list_rounds = []
            list_alredy_played = []

            while i < len(list_pairs):
                if list_pairs[i][0] in list_alredy_played or list_pairs[i][1] in list_alredy_played:
                    pass
                else:
                    list_alredy_played.append(list_pairs[i][0])
                    list_alredy_played.append(list_pairs[i][1])
                    list_rounds.append(list_pairs[i])
                i += 1
            
            list_pairs = [i for i in list_pairs if i not in list_rounds]

            r += 1
            self.round_dict["Round_" + str(r)] = list_rounds

        print(self.round_dict)
        return self.round_dict

    def play_game(self):
        show_rounds = View().show_round_informations(self.round_dict)
