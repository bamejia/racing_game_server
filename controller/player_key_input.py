import pygame
from model.pause_menu import pause
from model.direction import Dir
import global_variables as gv
import sys

pause_repeat = True
escape_repeat = True


def title_screen_input(events):
    global escape_repeat
    for event in events:
        keys = pygame.key.get_pressed()
        # num_of_keys = keys.count(True)

        if not keys[pygame.K_ESCAPE] and not keys[pygame.K_BACKSPACE]:
            escape_repeat = True

        if event.type == pygame.QUIT or (keys[pygame.K_ESCAPE] and escape_repeat):
            pygame.quit()
            sys.exit()


def player_input(events):
    global pause_repeat
    global escape_repeat

    player_input_dir = Dir.NONE
    keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not keys[pygame.K_RETURN] and not keys[pygame.K_t]:
        pause_repeat = True
    if (keys[pygame.K_ESCAPE] or keys[pygame.K_BACKSPACE]) and escape_repeat:
        escape_repeat = False
        return False
    if keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_s]:
        player_input_dir = Dir.NORTH
    elif keys[pygame.K_w] and keys[pygame.K_d] and not keys[pygame.K_a] and not keys[pygame.K_s]:
        player_input_dir = Dir.NORTHEAST
    elif keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s]:
        player_input_dir = Dir.EAST
    elif keys[pygame.K_d] and keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_w]:
        player_input_dir = Dir.SOUTHEAST
    elif keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d]:
        player_input_dir = Dir.SOUTH
    elif keys[pygame.K_a] and keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_d]:
        player_input_dir = Dir.SOUTHWEST
    elif keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_d]:
        player_input_dir = Dir.WEST
    elif keys[pygame.K_a] and not keys[pygame.K_s] and keys[pygame.K_w] and not keys[pygame.K_d]:
        player_input_dir = Dir.NORTHWEST
    else:
        player_input_dir = Dir.NONE

    if (keys[pygame.K_RETURN] or keys[pygame.K_t]) and pause_repeat:
        pause_repeat = False
        return True
    return player_input_dir


def player_input2(events):
    global pause_repeat
    global escape_repeat

    player_input_dir = Dir.NONE
    keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not keys[pygame.K_RETURN] and not keys[pygame.K_t]:
        pause_repeat = True
    if (keys[pygame.K_ESCAPE] or keys[pygame.K_BACKSPACE]) and escape_repeat:
        escape_repeat = False
        return False
    if keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
        player_input_dir = Dir.NORTH
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
        player_input_dir = Dir.NORTHEAST
    elif not keys[pygame.K_UP] and keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
        player_input_dir = Dir.EAST
    elif not keys[pygame.K_UP] and keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
        player_input_dir = Dir.SOUTHEAST
    elif not keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
        player_input_dir = Dir.SOUTH
    elif not keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        player_input_dir = Dir.SOUTHWEST
    elif not keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        player_input_dir = Dir.WEST
    elif keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        player_input_dir = Dir.NORTHWEST
    else:
        player_input_dir = Dir.NONE

    if (keys[pygame.K_RETURN] or keys[pygame.K_t]) and pause_repeat:
        pause_repeat = False
        return True

    return player_input_dir
