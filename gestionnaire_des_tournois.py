from controller.controller import Controller_game
from controller.controller_player import Controller_player


def main():
    play_tournament = Controller_game()
    tournament_settings = play_tournament.creat_tournament()
    tournament = tournament_settings[0]
    players_list = tournament_settings[1]
    round_list = tournament_settings[2]

    get_players = Controller_player()
    get_players.load_players_from_tournament(tournament, players_list)
    if len(round_list) == 0:
        get_players.get_players(tournament)
        play_tournament.create_list_rounds(tournament)
    else:
        play_tournament.load_rounds_from_tournament(tournament, round_list)
    
    
    play_tournament.play_rounds(tournament)
    play_tournament.classement()


main()
