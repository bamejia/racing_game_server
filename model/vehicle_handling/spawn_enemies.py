import random
import model.vehicle_handling.vehicle as v
from model.vehicle_handling.collision_and_boundaries import check_all_collision
import global_variables as gv

spawn_rate = 40  # higher is a lower spawn_rate
spawn_max = 17

tracker_cars = 0


def spawn_chance(vehicles, car_type="random", x=None, y=None, w=gv.ENEMY_WIDTH, l=gv.ENEMY_LENGTH):
    index = len(vehicles)
    if index >= spawn_max:
        return
    if x is not None:
        if random.randint(1, spawn_rate) == 1:
            vehicle = spawn_random_enemy(index, car_type, x, y, w, l, tracker_cars)
            if check_for_other_vehicle(vehicle, vehicles):  # if spawn area is occupied by another car, will not spawn
                return
            vehicles.append(vehicle)
    else:
        if random.randint(1, spawn_rate) == 1:
            x_placement = random.randint(round(gv.WINDOW_W * (1 - gv.ROAD_W_RATIO) / 2 + w),
                                         round(gv.WINDOW_W * (1 - gv.ROAD_W_RATIO) / 2 + gv.ROAD_W - w))
            vehicle = spawn_random_enemy(index, car_type, x_placement, y, w, l, tracker_cars)
            if check_for_other_vehicle(vehicle, vehicles):
                return
            vehicles.append(vehicle)


def spawn_random_enemy(index, car_type, x, y, w, l, tracker_count):
    global tracker_cars
    if tracker_count <= 0:
        pattern = "tracker"
    else:
        pattern = gv.CAR_TYPES[random.randint(2, len(gv.CAR_TYPES)-1)]
    if pattern == "tracker":
        tracker_cars += 1

    return v.Enemy(index, pattern, x, y, w, l)


def check_for_other_vehicle(vehicle, vehicles):
    if check_all_collision(vehicle, vehicles) is not None:
        return True
    return False

