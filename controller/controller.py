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
        self.tournament = Tournament()
        self.view = View()

    def creat_tournament(self):
        tournament_informations = self.view.get_tournament_start_informations()
        name = tournament_informations[0]
        place = tournament_informations[1]
        date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.tournament.modify_start_information(name, place, date_start)


    def get_players(self):
        while True:
            player_informations = self.view.get_player_informations()

            first_name = player_informations[0]
            family_name = player_informations[1]
            birth_date = player_informations[2]
            add_player = player_informations[3]

            player = Player(first_name, family_name, birth_date)
            self.tournament.add_player(player)

            players = self.tournament.give_len_list_players()

            if (add_player == "n") and (players < 2):
                self.view.add_more_players()
            elif (add_player == "n") and (players >= 2):
                break

        
    def round_estimation(self):

        # participants = self.tournament.give_list_players()
        
        
        player_1 = Player(first_name = "aa", family_name ="aa", birth_date = "05101992", score = 0)
        player_2 = Player(first_name = "bb", family_name ="bb", birth_date = "05101992", score = 0)
        player_3 = Player(first_name = "cc", family_name ="cc", birth_date = "05101992", score = 0)
        player_4 = Player(first_name = "dd", family_name ="dd", birth_date = "05101992", score = 0)
        player_5 = Player(first_name = "ee", family_name ="ee", birth_date = "05101992", score = 0)

        self.tournament.players_list = [player_1, player_2, player_3, player_4, player_5]
        participants_len = self.tournament.give_len_list_players()

        

        if (participants_len % 2) == 0:  #Si nombre des participant est paire il y a N-1 tours possibles
            max_round = participants_len - 1
            self.view.show_round_estimation(max_round)
        else:  #Si nombre des participant est impaire il y a N tours possibles, il faut ajouter un joueur fictif 
            max_round = participants_len
            self.view.show_round_estimation(max_round)

            player_repos = Player("Repos", "Repos", datetime.now().strftime("%d%m%Y"))
            self.view.add_player_repos()
            self.tournament.add_player(player_repos)

        participants = self.tournament.give_list_players()
        self.view.show_players(participants)


        return max_round
        
        
    def round_proposition(self, max_round):
        while True:
            round_proposition = self.view.get_round_proposition()

            if round_proposition <= 0 or round_proposition > int(max_round):
                round_proposition = self.view.get_round_proposition_error(max_round)
            else:
                self.tournament.modify_all_round_information(round_proposition)
                break

    def generate_round_name(self, i):
        name = "Round_" + str(i)
        return name

    def create_rounds(self):
        rounds = self.tournament.give_len_list_players()
        i = 1
        while i <= rounds:
            if i == 1:
                create_name = self.generate_round_name(i)
                create_date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                round = Round(name = create_name, date_start = create_date_start)
                players = self.tournament.give_list_players()
                self.shuffle_players(i, players)
                print(players)
            i += 1



    def play_round(self):
        pass

    
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

    def shuffle_players(self, round, players):

        if round == 1:
            random.shuffle(players)
        else:
            players.sort(key=lambda p: p.score, reverse=True) # p reprensent objet Player
        return players

        
        

        


    
    

