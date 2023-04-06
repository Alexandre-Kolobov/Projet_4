# import json
from models.tournament import Tournament
from controller.controller import Controller
from models.player import Player
from views.views import View
from itertools import combinations
import random


def main():
   
    play_tournament = Controller()
    play_tournament.creat_tournament()
    play_tournament.get_players()
    play_tournament.play_rounds()
    play_tournament.classement()

main()

# player_1 = Player("a", "a", "05101992", 0)
# player_2 = Player("b", "b", "05101992", 0)
# player_3 = Player("c", "c", "05101992", 0)
# player_4 = Player("d", "d", "05101992", 0)
# player_5 = Player("e", "e", "05101992", 0)
# player_6 = Player("f", "f", "05101992", 0)
# players = [player_1, player_2, player_3, player_4, player_5, player_6]

# players_bis = []
# players_bis = players


# l = 0

# while l < 1000:

#     for k in players:
#         k.ingame = False
#         list_test = []

#     for i in players:
#         if i.ingame == False:
            
#             for p in players:
#                 if i != p:
                    
#                     if p.ingame == False and i.ingame == False:
#                         if (p not in i.played_with) and (i not in p.played_with):
#                             p.ingame = True
#                             i.ingame = True
#                             list_test.append([i, p])

                                      
#     if len(list_test) == (len(players)//2):
#         print (list_test)   
#         for li in list_test:
#             li[0].played_with.append(li[1])
#             li[1].played_with.append(li[0])
#     else:
#         random.shuffle(players)
#                             # print (f"{i} vs {p}")
                            
#     l += 1


        

    

