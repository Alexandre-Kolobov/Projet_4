from controller.controller_tournament import Controller_tournament
from controller.controller_player import Controller_player
from controller.controller_round import Controller_round
from controller.controller_match import Controller_match


def main():
    tournament_controller = Controller_tournament()
    player_controller = Controller_player()
    round_controller = Controller_round()
    match_controller = Controller_match()

    tournament_informations = tournament_controller.create_tournament()

    tournament = tournament_informations[0]
    players_list = tournament_informations[1]
    round_list = tournament_informations[2]
    current_round = tournament_informations[3]

    player_controller.load_players_from_tournament(tournament, players_list)

    if current_round == 0: #  Si les rounds n'ont pas été commencé (on continue la création des joueurs)
        player_controller.get_players(tournament)
        rounds = round_controller.create_list_rounds(tournament)
        for round in rounds:
            tournament.update_current_round()
            players = tournament_controller.shuffle_players(tournament)
            matchs = match_controller.create_matchs(tournament, round, players)
            # matchs = tournament_controller.play_round(tournament, round)
            for match in matchs:
                match_controller.play_match(tournament, match)
            round_controller.finish_round(tournament, round)

    else:
        # rounds = round_controller.load_rounds(tournament, round_list)
        # for round in rounds:
        #     matchs = tournament_controller.play_round(tournament, round)
        #     for match in matchs:
        #         tournament_controller.play_match(tournament, match)
        for round in round_list:
            round_inormations = round_controller.load_round(tournament, round)
            round_to_load = round_inormations[0]
            matchs = round_inormations[1]

            for match in matchs:
                match_controller.load_match(tournament, round_to_load, match)
            
            if round_to_load.give_finish_status() == False:
                match_list = round_to_load.give_match_list()
                if len(match_list) == 0:
                    tournament.update_current_round()
                    players = tournament_controller.shuffle_players(tournament)
                    matchs = match_controller.create_matchs(tournament, round_to_load, players)
                    # matchs = tournament_controller.play_round(tournament, round)
                    for match in matchs:
                        match_controller.play_match(tournament, match)
                    round_controller.finish_round(tournament, round_to_load)
                    tournament.save_tournament()

                for match in match_list:
                    print("TEST AKO")
                    if match.check_if_match_played() == False:
                        match_controller.play_match(tournament, match)
                        tournament.save_tournament()

                round_controller.finish_round(tournament, round_to_load)
            tournament.save_tournament()



        


    
    
    # play_tournament.play_rounds(tournament)
    tournament_controller.classement(tournament)


main()
