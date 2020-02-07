import random
from model.vehicle_handling.vehicle import Enemy
from model.direction import Dir
from model.vehicle_handling.collision_and_boundaries import check_on_road


def enemy_input(vehicles):
    for i, item in enumerate(vehicles):
        if isinstance(vehicles[i], Enemy):
            choose_pattern(vehicles[i], vehicles)


def choose_pattern(enemy, vehicles):

    if random.randint(0, 80) == 0:

        """ depending on the car_type of the car, will choose respective method """
        if enemy.car_type == "random":
            random_pattern(enemy)
        elif enemy.car_type == "side to side":
            side_to_side_pattern(enemy)
        elif enemy.car_type == "up and down":
            up_and_down_pattern(enemy)
        elif enemy.car_type == "diagonal":
            diagonal_pattern(enemy)
        elif enemy.car_type == "tracker":
            tracker_pattern(enemy, vehicles)
        elif enemy.car_type == "static":
            static_pattern(enemy)
        elif enemy.car_type == "speed demon":
            speed_demon_pattern(enemy)

    """ keeps cars on the road """
    road_direction = enemy.is_next_to_road()
    if road_direction.value > 0:
        if enemy.input_direction.value > 0 and enemy.input_direction != Dir.NORTH:
            enemy.input_direction = Dir.inverse(road_direction)
    elif road_direction.value < 0:
        if enemy.input_direction.value < 0 and enemy.input_direction != Dir.SOUTH:
            enemy.input_direction = Dir.inverse(road_direction)


def random_pattern(enemy):
    chosen_move = random.randint(0, 8)
    if chosen_move == 1:
        enemy.input_direction = Dir.NORTH
    elif chosen_move == 2:
        enemy.input_direction = Dir.NORTHEAST
    elif chosen_move == 3:
        enemy.input_direction = Dir.EAST
    elif chosen_move == 4:
        enemy.input_direction = Dir.SOUTHEAST
    elif chosen_move == 5:
        enemy.input_direction = Dir.SOUTH
    elif chosen_move == 6:
        enemy.input_direction = Dir.SOUTHWEST
    elif chosen_move == 7:
        enemy.input_direction = Dir.WEST
    elif chosen_move == 8:
        enemy.input_direction = Dir.NORTHWEST
    else:
        enemy.input_direction = Dir.NONE


def side_to_side_pattern(enemy):
    chosen_move = random.randint(1, 2)

    if chosen_move == 1:
        enemy.input_direction = Dir.EAST
    elif chosen_move == 2:
        enemy.input_direction = Dir.WEST
    else:
        enemy.input_direction = Dir.NONE


def up_and_down_pattern(enemy):
    chosen_move = random.randint(1, 2)

    if chosen_move == 1:
        enemy.input_direction = Dir.NORTH
    elif chosen_move == 2:
        enemy.input_direction = Dir.SOUTH
    else:
        enemy.input_direction = Dir.NONE


def diagonal_pattern(enemy):
    chosen_move = random.randint(1, 5)

    if chosen_move == 1:
        enemy.input_direction = Dir.NORTHWEST
    elif chosen_move == 2:
        enemy.input_direction = Dir.NORTHEAST
    if chosen_move == 3:
        enemy.input_direction = Dir.SOUTHWEST
    elif chosen_move == 4:
        enemy.input_direction = Dir.SOUTHEAST
    else:
        enemy.input_direction = Dir.NONE


def tracker_pattern(enemy, vehicles):
    choice = random.randint(0, 1)
    player = vehicles[0]
    player2 = None
    if vehicles[1].car_type == "player2":
        player2 = vehicles[1]
        if choice == 1:
            player = player2

    player_half_width = int(round(player.w / 2))
    player_half_length = int(round(player.l / 2))
    enemy_half_width = int(round(enemy.w / 2))
    enemy_half_length = int(round(enemy.l / 2))

    if enemy.x + enemy_half_width < player.x + player_half_width:
        if enemy.y + enemy_half_length < player.y + player_half_length:
            enemy.input_direction = Dir.SOUTHEAST
        elif enemy.y + enemy_half_length > player.y + player_half_length:
            enemy.input_direction = Dir.NORTHEAST
        else:
            enemy.input_direction = Dir.EAST
    elif enemy.x + enemy_half_width > player.x + player_half_width:
        if enemy.y + enemy_half_length < player.y + player_half_length:
            enemy.input_direction = Dir.SOUTHWEST
        elif enemy.y + enemy_half_length > player.y + player_half_length:
            enemy.input_direction = Dir.NORTHWEST
        else:
            enemy.input_direction = Dir.WEST
    elif enemy.y + enemy_half_length < player.y + player_half_length:
        enemy.input_direction = Dir.SOUTH
    elif enemy.y + enemy_half_length > player.y + player_half_length:
        enemy.input_direction = Dir.NORTH
    else:
        enemy.input_direction = Dir.NONE


def static_pattern(enemy):
    pass


def speed_demon_pattern(enemy):
    chosen_move = random.randint(0, 3)

    if chosen_move == 1:
        enemy.input_direction = Dir.NORTHWEST
    elif chosen_move == 2:
        enemy.input_direction = Dir.NORTHEAST
    elif chosen_move == 3:
        enemy.input_direction = Dir.NORTH
    else:
        enemy.input_direction = Dir.NONE
