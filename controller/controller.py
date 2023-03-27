from models.player import Player
from views.views import View
from itertools import combinations
from datetime import datetime
from models.tournament import Round
from models.tournament import Game
import random

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

        if len(self.players) <= 1:
            add_more_players = View().add_more_players()
            self.get_players()

        return self.players
    
    def round_estimation(self):
        participants = self.get_players()
        show_players = View().show_players(self.players)

        if (len(participants) % 2) == 0:  #Si nombre des participant est paire il y a N-1 tours possibles
            max_round = int(len(participants) - 1)
            show_round_estimation = View().show_round_estimation(max_round)
            return max_round
        else:  #Si nombre des participant est impaire il y a N tours possibles
            max_round = int(len(participants))
            show_round_estimation = View().show_round_estimation(max_round)
            return max_round
        
    def round_proposition(self, max_round):
        round_proposition = View().get_round_proposition()

        while 0 > round_proposition >= max_round:
            round_proposition = View().get_round_proposition_error(max_round)
            round_proposition = View().get_round_proposition()

        return round_proposition

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

    def generate_list_round(self, round_proposition):
        list_rounds = []
        i = 0
        while i <= round_proposition:
            i += 1
            round_name = ("Round_" + str(i))
            
            list_rounds.append(Round(round_name))

        return list_rounds
    
    def play_rounds(self, list_rounds):
        bool_first_round = True
        for round in list_rounds:
            self.players = self.shuffle_players(bool_first_round, self.players)
            bool_first_round = False
            # ajouter input
            round.date_start = "05052023"
        
            self.generate_pairs(self.players)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        date_finish = current_time

        return date_finish

    def generate_pairs(self, players):
        i = 0
        list_games = []
        while i < len(players):
            if players[i].in_game:
                print(f"joueur {players[i]} joue déja")
            else:
                players[i].in_game = True
                p = i
                while p < len(players):
                    if players[p] in players[i].already_played_with:
                        print(f"joueur {players[i]} et jouer {players[p]} ont déja joué")
                    else:
                        if players[i] != players[p]:
                            print(f"joueur {players[i]} et jouer {players[p]} vont jouer ensemble")
                            players[i].already_played_with.append(players[p])
                            players[p].already_played_with.append(players[i])
                            players[p].in_game = True
                            game = Game(players[i], players[i].score, players[p], players[p].score)
                            list_games.append(game)

                            break
                    p += 1
            i +=1
        print(list_games)
                        


    def shuffle_players(self, bool_first_round, players):

        if bool_first_round:
            random.shuffle(players)
        else:
            players.sort(key=lambda p: p.score, reverse=True) # p reprensent objet Player
        
        print (players)
        return players

        
        

        


    
    

