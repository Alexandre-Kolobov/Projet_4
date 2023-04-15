from controller.controller import Controller_game
from controller.controller import Controller_player


def main():
    play_tournament = Controller_game()
    play_tournament.creat_tournament()

    get_players = Controller_player()
    get_players.get_players()
    get_players.check_number_players()
    
    play_tournament.create_list_rounds()
    play_tournament.play_rounds()
    play_tournament.classement()


main()
