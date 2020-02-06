import pygame

from model.pause_menu import pause
from view.game_view import GameView
from model.game_model import GameModel, check_if_player_is_alive
from controller.player_key_input import player_input, player_input2
from controller.enemy_input import enemy_input
from model.vehicle_handling.spawn_enemies import spawn_chance
from global_variables import MOVEMENT_PATTERNS
import time


def p2_start(window):
    game_view = GameView(window)
    game_model = GameModel(num_players=2)

    all_player_inputs = [None, None]
    while True:
        events = pygame.event.get()

        all_player_inputs[0] = player_input(events)
        if game_model.player2 is not None:
            all_player_inputs[1] = player_input2(events)
        # print(self.game_model.player.cur_x_vel, self.game_model.player.reaction_x_vel, self.game_model.player.cur_y_vel, self.game_model.player.reaction_y_vel)

        if True in all_player_inputs:
            will_escape = pause(True)
            if will_escape:
                break
        elif False in all_player_inputs:
            break
        else:
            enemy_input(game_model.vehicles)

            game_model.update(all_player_inputs)
            game_view.update(game_model.vehicles)

            if not check_if_player_is_alive(game_model.player):
                time.sleep(2.5)
                break
            if game_model.player2 is not None and not check_if_player_is_alive(game_model.player2):
                time.sleep(2.5)
                break

        # print(window.clock.get_fps())
        window.clock.tick(120)