# from win32api import GetSystemMetrics
from enum import Enum

import pygame


# game running speed
GAME_FPS = 60
ACCEL_SPEED_MULTIPLIER = 120 / GAME_FPS

# window variables
WINDOW_NAME = "Racing Game"
WINDOW_X_POS = 300
WINDOW_Y_POS = 100
WINDOW_W_RATIO = 5/8
WINDOW_L_RATIO = 7/8
# WINDOW_W, WINDOW_L = WINDOW_SIZE = round(GetSystemMetrics(0) * WINDOW_W_RATIO),\
#                                                           round(GetSystemMetrics(1) * WINDOW_L_RATIO)
# print(WINDOW_W, WINDOW_L, WINDOW_SIZE)

WINDOW_W, WINDOW_L = WINDOW_SIZE = 1024, 900
WINDOW_W, WINDOW_L = WINDOW_SIZE = 1024, 768

# title screen variables
TITLE_TEXT = "RACING GAME"
TITLE_TEXT_SIZE = 140
TITLE_FONT = None
AUTHOR_TEXT = "by bamxmejia"
AUTHOR_TEXT_SIZE = 80
AUTHOR_FONT = None
# BUTTON_TEXTS = (
#     "Single Player",
#     "Local 2 Player",
#     "Online MultiPlayer",
#     "Exit"
# )
BUTTON_TEXT_SIZE = 75
BUTTON_FONT = None

# road variables
ROAD_W_RATIO = 6/12  #3/5
ROAD_W, ROAD_L = ROAD_DIMENSIONS = (round(WINDOW_W*ROAD_W_RATIO), round(WINDOW_L))
ROAD_X_PLACEMENT = (round(WINDOW_W * (1 - ROAD_W_RATIO) / 2))

# colors
WHITE = (255, 255, 255)
VERY_LIGHT_GREY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 0, 150)
TANISH_YELLOW = (255, 255, 100)
BRIGHT_RED = (255,0,0)
RED = (210, 0, 0)
DARK_RED = (125, 0, 0)
YELLOW = (255, 255, 0)
TANISH_GREY = (125, 125, 100)
ORANGE = (255, 120, 0)
DARK_ORANGE = (255, 120, 0)
LIGHT_GREY_BLUE = (125, 150, 150)
PEACH_PINK = (255, 152, 154)
PEACH = (255, 161, 100)
MID_DARK_PEACH = (255, 157, 0)
DARK_PEACH = (238, 138, 49)
BROWN = (185, 113, 62)
TURQOISE = (0, 152, 154)
GREEN = (0, 175, 0)
DARK_GREEN = (0, 100, 40)
TAN = (255, 195, 155)

# traffic variables
TRAFFIC_SPEED = 3 * ACCEL_SPEED_MULTIPLIER  # 3 or 2
FRICTION = 0.083 * ACCEL_SPEED_MULTIPLIER
REACTION_FRICTION = 0.083 * ACCEL_SPEED_MULTIPLIER
FRICTION_MARKER = 0  # round(12 / ACCEL_SPEED_MULTIPLIER)
REACTION_SPEED_MAX = 12 * ACCEL_SPEED_MULTIPLIER

# player defaults
# PLAYER_WIDTH = round(WINDOW_W / 32)
PLAYER_WIDTH = 25
PLAYER_LENGTH = 54
PLAYER_ACCELERATION = 0.115 * ACCEL_SPEED_MULTIPLIER
PLAYER_MAX_SPEED = 4.5 * ACCEL_SPEED_MULTIPLIER
PLAYER_HANDLING = 0.15 * ACCEL_SPEED_MULTIPLIER
PLAYER_MAX_HANDLING = 4 * ACCEL_SPEED_MULTIPLIER
PLAYER_STARTING_HEALTH = 1000

# enemy defaults
ENEMY_WIDTH = PLAYER_WIDTH
ENEMY_LENGTH = PLAYER_LENGTH
ENEMY_ACCELERATION = 0.115 * ACCEL_SPEED_MULTIPLIER
ENEMY_MAX_SPEED = 4 * ACCEL_SPEED_MULTIPLIER
ENEMY_HANDLING = 0.15 * ACCEL_SPEED_MULTIPLIER
ENEMY_MAX_HANDLING = 2 * ACCEL_SPEED_MULTIPLIER
ENEMY_STARTING_HEALTH = PLAYER_STARTING_HEALTH


# car types
class CarType(Enum):
    PLAYER_1 = "player 1"
    PLAYER_2 = "player 2"
    RANDOM = "random"
    SIDE_TO_SIDE = "side to side"
    UP_AND_DOWN = "up and down"
    DIAGONAL = "diagonal"
    TRACKER = "tracker"
    STATIC = "static"
    SPEED_DEMON = "speed demon"


# car lengths and widths
CAR_SIZES = {
    CarType.PLAYER_1: (PLAYER_WIDTH, PLAYER_LENGTH),
    CarType.PLAYER_2: (PLAYER_WIDTH, PLAYER_LENGTH),
    CarType.RANDOM: (ENEMY_WIDTH, ENEMY_LENGTH),
    CarType.SIDE_TO_SIDE: (ENEMY_WIDTH, ENEMY_LENGTH),
    CarType.UP_AND_DOWN: (ENEMY_WIDTH, ENEMY_LENGTH),
    CarType.DIAGONAL: (ENEMY_WIDTH, ENEMY_LENGTH),
    CarType.TRACKER: (ENEMY_WIDTH, ENEMY_LENGTH),
    CarType.STATIC: (ENEMY_WIDTH, ENEMY_LENGTH),
    CarType.SPEED_DEMON: (ENEMY_WIDTH, ENEMY_LENGTH),
}

# image paths
CAR_IMAGE_PATHS = {
    CarType.PLAYER_1: "Images/car/red car.png",
    CarType.PLAYER_2: "Images/car/blue car.png",
    CarType.RANDOM: "Images/car/purple car.png",
    CarType.SIDE_TO_SIDE: "Images/car/orange car.png",
    CarType.UP_AND_DOWN: "Images/car/yellow car.png",
    CarType.DIAGONAL: "Images/car/pink car.png",
    CarType.TRACKER: "Images/car/black car.png",
    CarType.STATIC: "Images/car/green car.png",
    CarType.SPEED_DEMON: "Images/car/white car.png"
}

# power up types
POWER_UPS = (
    "force bubble",
    "one shot",
    "speed"
)

# for testing
BOTTOM_BORDER = True
