from model.vehicle_handling.vehicle_movement_handler import vehicle_movement_handler
import global_variables as gv
from model.vehicle_handling import off_screen_handling
from model.direction import Dir
import json


class Vehicle:
    def __init__(self, index, movement_pattern, x, y, w, l,
                 acceleration, max_speed, handling, max_handling,  _health,
                 input_x_vel=0, input_y_vel=0, input_direction=Dir.NONE,
                 reaction_x_vel=0, reaction_y_vel=0,
                 cur_x_vel=0, cur_y_vel=0, cur_direction=Dir.NONE,
                 friction_marker=gv.FRICTION_MARKER,
                 friction_count=0, acceleration_count=0, handling_count=0, score=0):
        self.movement_pattern = movement_pattern
        self.index = index
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.max_speed = max_speed
        self.cur_x_vel = cur_x_vel  # current x velocity
        self.cur_y_vel = cur_y_vel
        self.cur_direction = cur_direction
        self.handling = handling
        self.max_handling = max_handling
        self.input_x_vel = input_x_vel
        self.input_y_vel = input_y_vel
        self.input_direction = input_direction
        self.acceleration = acceleration
        self.health = _health
        self.reaction_x_vel = reaction_x_vel
        self.reaction_y_vel = reaction_y_vel
        self.acceleration_count = acceleration_count
        self.handling_count = handling_count
        self.friction_count = friction_count
        self.friction_marker = friction_marker
        self.score = score

    """ METHODS """
    # def to_json(self):
    #     return json.dumps(self, default=lambda o: o.dict,
    #                       sort_keys=True, indent=4)

    def update_location(self, other_vehicles):
        vehicle_movement_handler(self, other_vehicles)

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def is_next_to_road(self):
        if abs(self.cur_x_vel) >= self.max_handling:
            if self.x + self.cur_x_vel < gv.ROAD_X_PLACEMENT:
                return Dir.WEST
            elif self.x + self.w + self.cur_x_vel > gv.ROAD_X_PLACEMENT + gv.ROAD_W:
                return Dir.EAST
        else:
            if self.x + self.cur_x_vel - self.handling < gv.ROAD_X_PLACEMENT:
                return Dir.WEST
            elif self.x + self.w + self.cur_x_vel + self.handling > gv.ROAD_X_PLACEMENT + gv.ROAD_W:
                return Dir.EAST
        return Dir.NONE
    
    """ GETTERS """
    @property
    def health(self):
        return self._health
    
    """ SETTERS """
    @health.setter
    def health(self, health):
        self._health = health
        if self.health < 0:
            self._health = 0

    def x_input_against_x_reaction(self):
        if self.reaction_x_vel < 0 and self.input_x_vel < 0:
            self.reaction_x_vel = self.reaction_x_vel - self.input_x_vel
            if self.reaction_x_vel > 0:
                self.reaction_x_vel = 0
        elif self.reaction_x_vel > 0 and self.input_x_vel > 0:
            self.reaction_x_vel = self.reaction_x_vel - self.input_x_vel
            if self.reaction_y_vel < 0:
                self.reaction_y_vel = 0
        if self.reaction_x_vel > 0 and self.input_x_vel < 0:
            self.reaction_x_vel = self.reaction_x_vel + self.input_x_vel
            if self.reaction_y_vel < 0:
                self.reaction_y_vel = 0
        elif self.reaction_x_vel < 0 and self.input_x_vel > 0:
            self.reaction_x_vel = self.reaction_x_vel + self.input_x_vel
            if self.reaction_y_vel > 0:
                self.reaction_y_vel = 0

    def y_input_against_y_reaction(self):
        if self.reaction_y_vel > 0 and self.input_y_vel < 0:
            self.reaction_y_vel = self.reaction_y_vel + self.input_y_vel
            if self.reaction_y_vel < 0:
                self.reaction_y_vel = 0
        elif self.reaction_y_vel < 0 and self.input_y_vel > 0:
            self.reaction_y_vel = self.reaction_y_vel + self.input_y_vel
            if self.reaction_y_vel > 0:
                self.reaction_y_vel = 0
        if self.reaction_y_vel < 0 and self.input_y_vel < 0:
            self.reaction_y_vel = self.reaction_y_vel - self.input_y_vel
            if self.reaction_y_vel > 0:
                self.reaction_y_vel = 0
        elif self.reaction_y_vel > 0 and self.input_y_vel > 0:
            self.reaction_y_vel = self.reaction_y_vel - self.input_y_vel
            if self.reaction_y_vel < 0:
                self.reaction_y_vel = 0

    def acceleration_on_input_x_vel(self, acceleration):
        if self.input_x_vel + acceleration > self.max_handling:
            return
        elif self.input_x_vel + acceleration < -1 * self.max_handling:
            return
        else:
            self.input_x_vel += acceleration

    def friction_on_input_x_vel(self, input_x_vel):
        self.input_x_vel = input_x_vel

    def acceleration_on_input_y_vel(self, acceleration):
        if self.input_y_vel + acceleration > int(round(self.max_speed / 2)):
            return
        elif self.input_y_vel + acceleration < -1 * self.max_speed:
            return
        else:
            self.input_y_vel += acceleration

    def off_road_on_input_y_vel(self, off_road_y):
        if self.input_y_vel + off_road_y > self.max_speed:
            return
        elif self.input_y_vel + off_road_y < -1 * self.max_speed:
            return
        else:
            self.input_y_vel += off_road_y

    def friction_on_input_y_vel(self, input_y_vel):
        self.input_y_vel = input_y_vel


class Player(Vehicle):
    def __init__(self, index, movement_pattern ="player", x=400, y=400, w=gv.PLAYER_WIDTH, l=gv.PLAYER_LENGTH,
                 acceleration=gv.PLAYER_ACCELERATION, max_speed=gv.PLAYER_MAX_SPEED, handling=gv.PLAYER_HANDLING,
                 max_handling=gv.PLAYER_MAX_HANDLING, _health=gv.PLAYER_STARTING_HEALTH,
                 input_x_vel=0, input_y_vel=0, input_direction=Dir.NONE,
                 reaction_x_vel=0, reaction_y_vel=0,
                 cur_x_vel=0, cur_y_vel=0, cur_direction=Dir.NONE,
                 friction_marker=gv.FRICTION_MARKER,
                 friction_count=0, acceleration_count=0, handling_count=0, score=0):
        super().__init__(index, movement_pattern, x, y, w, l, acceleration, max_speed, handling, max_handling, _health,
                         input_x_vel, input_y_vel, input_direction,
                         reaction_x_vel, reaction_y_vel,
                         cur_x_vel, cur_y_vel, cur_direction,
                         friction_marker,
                         friction_count, acceleration_count, handling_count, score)

    """ METHODS """
    def is_below_screen(self):
        if off_screen_handling.check_if_below_screen(self):
            return True
        return False

    @staticmethod
    def from_json(json_string):
        json_dict = json.loads(json_string)
        return Player(**json_dict)


class Enemy(Vehicle):
    def __init__(self, index, movement_pattern="random", x=None, y=None, w=gv.ENEMY_WIDTH, l=gv.ENEMY_LENGTH,
                 acceleration=gv.ENEMY_ACCELERATION, max_speed=gv.ENEMY_MAX_SPEED, handling=gv.ENEMY_HANDLING,
                 max_handling=gv.ENEMY_MAX_HANDLING, _health=gv.ENEMY_STARTING_HEALTH, input_x_vel=0, input_y_vel=0,
                 input_direction=Dir.NONE,
                 reaction_x_vel=0, reaction_y_vel=0,
                 cur_x_vel=0, cur_y_vel=0, cur_direction=Dir.NONE,
                 friction_marker=gv.FRICTION_MARKER,
                 friction_count=0, acceleration_count=0, handling_count=0, score=0):
        if x is not None and y is None:
            super().__init__(index, movement_pattern, x, -l-1, w, l, acceleration, max_speed, handling, max_handling,
                             _health, input_x_vel, input_y_vel, input_direction,
                             reaction_x_vel, reaction_y_vel,
                             cur_x_vel, cur_y_vel, cur_direction,
                             friction_marker,
                             friction_count, acceleration_count, handling_count, score)
        elif x is not None or y is not None:
            super().__init__(index, movement_pattern, x, y, w, l, acceleration, max_speed, handling, max_handling,
                             _health, input_x_vel, input_y_vel, input_direction,
                             reaction_x_vel, reaction_y_vel,
                             cur_x_vel, cur_y_vel, cur_direction,
                             friction_marker,
                             friction_count, acceleration_count, handling_count, score)
        else:
            super().__init__(index, movement_pattern, 30, 30, w, l, acceleration, max_speed, handling, max_handling,
                             _health, input_x_vel, input_y_vel, input_direction,
                             reaction_x_vel, reaction_y_vel,
                             cur_x_vel, cur_y_vel, cur_direction,
                             friction_marker,
                             friction_count, acceleration_count, handling_count, score)

    """ METHODS """
    def check_to_despawn(self, vehicles):
        if off_screen_handling.check_if_below_screen(self):
            off_screen_handling.despawn(self, vehicles)

    @staticmethod
    def from_json(json_string):
        json_dict = json.loads(json_string)
        return Enemy(**json_dict)

