# import json
from models.tournament import Tournament
from controller.controller import Controller
from models.player import Player
from views.views import View
from itertools import combinations



def main():
   
    play_tournament = Controller()
    play_tournament.creat_tournament()
    play_tournament.get_players()
    play_tournament.create_list_rounds()
    play_tournament.classement()

main()
        

    

