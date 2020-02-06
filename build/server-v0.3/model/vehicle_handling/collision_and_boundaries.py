from global_variables import WINDOW_W, WINDOW_L, ROAD_X_PLACEMENT, ROAD_W, BOTTOM_BORDER


def check_collision(vehicle, other_vehicle):
    step = 100
    current_width = 0
    current_length = 0
    while current_width <= vehicle.w:
        while current_length <= vehicle.l:
            if other_vehicle.x <= vehicle.x + current_width <= other_vehicle.x + other_vehicle.w and \
                    other_vehicle.y <= vehicle.y + current_length <= other_vehicle.y + other_vehicle.l:
                return True
            if current_length + step > vehicle.l and current_length != vehicle.l:
                current_length = vehicle.l
            else:
                current_length += step
        current_length = 0
        if current_width + step > vehicle.w and current_width != vehicle.w:
            current_width = vehicle.w
        else:
            current_width += step
    return False


def check_all_collision(vehicle, other_vehicles):
    index_ignored = vehicle.index
    count = 0
    while count < len(other_vehicles):
        if count != index_ignored:
            if check_collision(vehicle, other_vehicles[count]):
                return other_vehicles[count]
        count += 1
    return None


def check_boundary(vehicle):
    if vehicle.x < 0:
        vehicle.x = 0
    elif vehicle.x + vehicle.w > WINDOW_W:
        vehicle.x = WINDOW_W - vehicle.w
    if vehicle.y < -vehicle.l - 1:
        vehicle.y = -vehicle.l - 1
    if BOTTOM_BORDER:
        if vehicle.y + vehicle.l > WINDOW_L:
            vehicle.y = WINDOW_L - vehicle.l


def check_on_road(vehicle):
    if vehicle.x > ROAD_X_PLACEMENT and vehicle.x + vehicle.w < ROAD_X_PLACEMENT + ROAD_W:
        return True
    return False
