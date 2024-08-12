import math


class DistanceCalculator:
    INVALID_INPUT_MESSAGE = ('Invalid Input: Instructions may only contain integers '
                             'and the letters "F", "B", "R", or "L".')

    INSTRUCTION_DIRECTIONS = {
        'F': (0, 1),
        'B': (0, -1),
        'L': (1, 0),
        'R': (-1, 0)
    }

    COMPASS_DIRECTIONS = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    INSTRUCTION_MAP = {
        'NF': 'N', 'NB': 'S', 'NR': 'E', 'NL': 'W',
        'SF': 'S', 'SB': 'N', 'SR': 'W', 'SL': 'E',
        'EF': 'E', 'EB': 'W', 'ER': 'S', 'EL': 'N',
        'WF': 'W', 'WB': 'E', 'WR': 'N', 'WL': 'S',
    }

    def __init__(self):
        pass

    def calculate_fixed_direction_distance(self, instructions):
        x, y = 0, 0

        i = 0
        while i < len(instructions):
            if not instructions[i].isdigit() and instructions[i] not in "FBRL":
                raise ValueError(self.INVALID_INPUT_MESSAGE)

            steps = ""
            while i < len(instructions) and instructions[i].isdigit():
                steps += instructions[i]
                i += 1

            if steps == "":
                steps = 0

            if instructions[i] in self.INSTRUCTION_DIRECTIONS:
                dx, dy = self.INSTRUCTION_DIRECTIONS[instructions[i]]
                x += dx * int(steps)
                y += dy * int(steps)
            else:
                raise ValueError(self.INVALID_INPUT_MESSAGE)

            i += 1

        return math.sqrt(x**2 + y**2)

    def calculate_relative_direction_distance(self, instructions):
        x, y = 0, 0
        instruction = "N"

        i = 0
        while i < len(instructions):
            if not instructions[i].isdigit() and instructions[i] not in "FBRL":
                raise ValueError(self.INVALID_INPUT_MESSAGE)

            steps = ""
            while i < len(instructions) and instructions[i].isdigit():
                steps += instructions[i]
                i += 1

            if steps == "":
                steps = 0

            instruction_key = instruction + instructions[i]
            if instruction_key in self.INSTRUCTION_MAP:
                instruction = self.INSTRUCTION_MAP[instruction_key]
                dx, dy = self.COMPASS_DIRECTIONS[instruction]
                x += dx * int(steps)
                y += dy * int(steps)
            else:
                raise ValueError(self.INVALID_INPUT_MESSAGE)

            i += 1

        return math.sqrt(x**2 + y**2)
