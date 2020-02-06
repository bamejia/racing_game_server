from enum import Enum
from enum import unique

@unique
class Dir(Enum):
    NONE = 0
    NORTH = 1
    NORTHEAST = 2
    EAST = 3
    SOUTHEAST = 4
    SOUTH = -1
    SOUTHWEST = -2
    WEST = -3
    NORTHWEST = -4

    @staticmethod
    def opposite(input_dir):
        opposite = input_dir.value * -1
        # for direct in Dir:
        #     if direct.value == opposite:
        #         return direct
        return Dir(opposite)

    @staticmethod
    def inverse(input_dir):
        if input_dir == Dir.NONE or input_dir == Dir.NORTH or input_dir == Dir.SOUTH:
            return input_dir
        if input_dir == Dir.NORTHWEST:
            return Dir.NORTHEAST
        if input_dir == Dir.NORTHEAST:
            return Dir.NORTHWEST
        if input_dir == Dir.SOUTHWEST:
            return Dir.SOUTHEAST
        if input_dir == Dir.SOUTHEAST:
            return Dir.SOUTHWEST
        if input_dir == Dir.EAST:
            return Dir.WEST
        if input_dir == Dir.WEST:
            return Dir.EAST


