from controller.controller_tournament import Controller_tournament
from controller.controller_player import Controller_player
from controller.controller_round import Controller_round
from controller.controller_match import Controller_match


def main():
    player_controller = Controller_player()
    round_controller = Controller_round()
    match_controller = Controller_match()
    tournament_controller = Controller_tournament(player_controller, round_controller, match_controller)
    tournament_controller.view_tournament.show_welcome()
    while True:
        run_again = tournament_controller.run()
        if run_again is False:
            break


main()
