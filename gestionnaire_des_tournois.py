from controller.controller import Controller


def main():
    play_tournament = Controller()
    play_tournament.creat_tournament()
    play_tournament.get_players()
    play_tournament.round_estimation()
    play_tournament.create_list_rounds()
    play_tournament.play_rounds()
    play_tournament.classement()


main()
