from models.player import Player
from views.views import View
from itertools import combinations
from datetime import datetime
from models.tournament import Tournament
from models.round import Round
from models.match import Match

import random

match_counter = 0

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
        # while True:
        #     player_informations = self.view.get_player_informations()

        #     first_name = player_informations[0]
        #     family_name = player_informations[1]
        #     birth_date = player_informations[2]
        #     add_player = player_informations[3]

        #     player = Player(first_name, family_name, birth_date)
        #     self.tournament.add_player(player)
        #     tournament_name = self.tournament.give_tournament_name()
        #     player.save_players_json(tournament_name)

        #     if (add_player == "n"):
        #         break

        self.get_players_test()
        self.round_estimation()

    def get_players_test(self):
        player_1 = Player("a", "a", "05101992")
        self.tournament.add_player(player_1)
        player_2 = Player("b", "b", "05101992")
        self.tournament.add_player(player_2)
        player_3 = Player("c", "c", "05101992")
        self.tournament.add_player(player_3)
        player_4 = Player("d", "d", "05101992")
        self.tournament.add_player(player_4)
        player_5 = Player("e", "e", "05101992")
        self.tournament.add_player(player_5)
        player_6 = Player("f", "f", "05101992")
        self.tournament.add_player(player_6)
        player_7 = Player("g", "g", "05101992")
        self.tournament.add_player(player_7)
        player_8 = Player("h", "h", "05101992")
        self.tournament.add_player(player_8)
        
    def round_estimation(self):

        participants_len = self.tournament.give_len_list_players()
        round_all = self.tournament.give_round_all_information()

        if (participants_len % 2) == 0:  #Si nombre des participant est paire il y a N-1 tours possibles
            max_round = participants_len - 1
            if max_round >= round_all:
                self.view.show_round_estimation(round_all)
            else:
                self.view.show_round_negative_estimation(round_all)
                self.get_players()
        else:  #Si nombre des participant est impaire, il faut ajouter des joueurs
            self.view.show_round_negative_estimation(round_all)
            self.get_players()
            

        participants = self.tournament.give_list_players()
        self.view.show_players(participants)

    def generate_round_name(self, i):
        name = "Round_" + str(i)
        return name
    
    def generate_match_name(self):
        global match_counter
        match_counter += 1
        name = "Match_" + str(match_counter)
        return name
    
    def create_list_rounds(self):
        rounds = self.tournament.give_round_all_information()
        i = 1 
        
        while i <= rounds:
            round_name = self.generate_round_name(i)
            round = Round(name = round_name)
            self.tournament.add_round(round)
            i += 1

    def play_rounds(self):
        rounds = self.tournament.give_round_list()
        for round in rounds:
            if not round.finish_status:
                round_date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                round.add_date_start(round_date_start)
                

    # def play_rounds_old(self):
    #     rounds = self.tournament.give_round_all_information()
    #     i = 1
    
    #     while i <= rounds:
    #         round_name = self.generate_round_name(i)
    #         round_date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #         round = Round(name = round_name, date_start = round_date_start)

    #         matchs = self.create_matchs(i)

    #         self.view.show_round(matchs, round_name)
            
    #         for match in matchs:
    #             player_1 = match.give_player_1()
    #             player_2 = match.give_player_2()
                
    #             player_1_name = player_1.give_player_name()
    #             player_2_name = player_2.give_player_name()

    #             match_result = self.view.play_match(player_1_name, player_2_name)
    #             match_result_dict = self.give_score(player_1_name, player_2_name, match_result)

    #             player_1.update_player_score(match_result_dict[player_1_name])
    #             player_2.update_player_score(match_result_dict[player_2_name])

    #             match.update_player_score(match_result_dict[player_1_name], match_result_dict[player_2_name])

    #             tournament_name = self.tournament.give_tournament_name()
    #             match.save_matchs_json(tournament_name)

    #             round.add_match(match)


    #         # print(round.__dict__)
    #         round_date_finish = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #         round.add_date_finish(round_date_finish)
    #         self.tournament.add_round(round)
            
    #         i += 1

    #     tournament_date_finish = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #     self.tournament.add_date_finish(tournament_date_finish)
    #     # print(self.tournament.__dict__)

    def create_matchs(self, round):
        matchs = []
        while True:
            players = self.shuffle_players(round)

            for player in players:
                player.update_ingame_status(False)
                temp_pairs_list = []

            for i in players:
                if i.give_ingame_status() == False:
                    for p in players:
                        if (i != p) and (p.give_ingame_status() == False) and (i.give_ingame_status() == False):
                            if (i.check_played_with(p) == False) and (p.check_played_with(i) == False):
                                
                                i.update_ingame_status(True)
                                p.update_ingame_status(True)
                                temp_pairs_list.append([i, p])
            

            pairs_by_round = len(players)/2
            if len(temp_pairs_list) == pairs_by_round:  #on obtiens nombre de pairs max par round
                   
                for temp in temp_pairs_list:
                    temp[0].add_played_with(temp[1])
                    temp[1].add_played_with(temp[0])

                    create_match_name = self.generate_match_name()
                    match = Match(create_match_name, temp[0], temp[1], temp[0].give_player_score(), temp[1].give_player_score())
                    matchs.append(match)
                 
                return matchs


    def check_played_match(self, matchs):
        for round in self.tournament.give_round_list():
            for match in round.give_match_list():
                for i in matchs:
                    if match == i:
                        return True


    def shuffle_players(self, round):
        players = self.tournament.give_list_players()
        players_len = self.tournament.give_len_list_players()

        if round == 1:
            random.shuffle(players)
        else:
            random_numbers = random.sample(range(0,players_len),players_len)
            for player in players:
                player.add_random_number(random_numbers.pop())
            
            players.sort(key=lambda p: (p.score, p.random_number), reverse=True) # p reprensent objet Player
        return players

        
    def give_score(self, player_1_name, player_2_name, match_result):
            match_result_dict = {}
            if  match_result == player_1_name:
                match_result_dict = {player_1_name : 1, player_2_name : 0}
                return match_result_dict
            elif  match_result == player_2_name:
                match_result_dict = {player_1_name : 0, player_2_name : 1}
                return match_result_dict
            else:
                match_result_dict = {player_1_name : 0.5, player_2_name : 0.5}
                return match_result_dict
    
    def classement(self):
        players = self.tournament.give_list_players()
        players.sort(key=lambda p: (p.score, p.random_number), reverse=True)

        place = 1
        for player in players:
            score = player.give_player_score()
            self.view.show_classment(player, place, score)
            place += 1


