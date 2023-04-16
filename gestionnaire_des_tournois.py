from controller.controller import Controller_game
from controller.controller_player import Controller_player


def main():
    play_tournament = Controller_game()
    tournament = play_tournament.creat_tournament()

    get_players = Controller_player(tournament)
    get_players.get_players()
    get_players.check_number_players()
    
    play_tournament.create_list_rounds()
    play_tournament.play_rounds()
    play_tournament.classement()


main()
