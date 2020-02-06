import pygame
from model.game_model import check_if_player_is_alive
from controller.enemy_input import enemy_input
import time


def game_thread(game):
    game_model, all_player_inputs, lock, has_ended = game
    clock = pygame.time.Clock()
    while True:
        lock.acquire()
        if game_model.ready:
            enemy_input(game_model.vehicles)
            if False in all_player_inputs:
                print("Game has ended")
                lock.release()
                break
            if has_ended[0]:
                print("Game h4s ended")
                lock.release()
                break
            # print(self.game_model.player.cur_x_vel, self.game_model.player.reaction_x_vel, self.game_model.player.cur_y_vel, self.game_model.player.reaction_y_vel)

            game_model.update(all_player_inputs)

            if not check_if_player_is_alive(game_model.player) or\
                    not check_if_player_is_alive(game_model.player2):
                time.sleep(2.5)
                lock.release()
                has_ended[0] = True
                break
            lock.release()
        else:
            lock.release()
        # print(clock.get_fps())
        clock.tick(120)
