from models.player import Player
from views.views import View
from itertools import combinations
from datetime import datetime
from models.tournament import Tournament
from models.round import Round
from models.match import Match

import random

class Controller:
    def __init__(self):
        self.tournaments = []

    def creat_tournament(self):
        tournament_informations = View().get_tournament_start_informations()
        name = tournament_informations[0]
        place = tournament_informations[1]
        date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        tournament = Tournament(name, place, date_start)
        self.tournaments.append(tournament)

    def get_players(self):

        player_informations = View().get_player_informations()

        first_name = player_informations[0]
        family_name = player_informations[1]
        birth_date = player_informations[2]
        add_player = player_informations[3]

        player = Player(first_name, family_name, birth_date)
        Tournament().add_player(player)

        if add_player == "y":
            self.get_players()

        if len(self.players) <= 1:
            View().add_more_players()
            self.get_players()

        print(Tournament.players_list)
    
    def round_estimation(self):
        
        # player_1 = Player(first_name = "aa", family_name ="aa", birth_date = "05101992", score = 0)
        # player_2 = Player(first_name = "bb", family_name ="bb", birth_date = "05101992", score = 0)
        # player_3 = Player(first_name = "cc", family_name ="cc", birth_date = "05101992", score = 0)
        # player_4 = Player(first_name = "dd", family_name ="dd", birth_date = "05101992", score = 0)
        # player_5 = Player(first_name = "ee", family_name ="ee", birth_date = "05101992", score = 0)
        # player_6 = Player(first_name = "Repos", family_name ="Repos", birth_date = "05101992", score = 0)

        # self.players = [player_1, player_2, player_3, player_4, player_5, player_6]

        participants = self.get_players()
        participants = self.players
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
        list_match = []
        for round in list_rounds:
            self.players = self.shuffle_players(bool_first_round, self.players)
            bool_first_round = False
            # ajouter input
            round.date_start = "05052023"
        
            self.generate_pairs(self.players, list_match)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        date_finish = current_time

        return date_finish

    def generate_pairs(self, players, list_match):
        
        i = 0 
        while i < len(players):
            if (players[i], players[i+1]) or (players[i+1], players[i]) in list_match:
                players = self.shuffle_players(False, players)
            else:
                list_match.append((players[i], players[i+1]))
                i += 2
                print(f"joueur {players[i]} et jouer {players[p]} vont jouer ensemble")
                players[i].score = players[i].score + int(input(f"entre le score pour {players[i]}:"))
                players[p].score = players[p].score + int(input(f"entre le score pour {players[p]}:"))
        
        
        print (list_match)

        return list_match

    def shuffle_players(self, bool_first_round, players):

        if bool_first_round:
            random.shuffle(players)
        else:
            players.sort(key=lambda p: p.score, reverse=True) # p reprensent objet Player
            
        
        print (players)
        return players

        
        

        


    
    

