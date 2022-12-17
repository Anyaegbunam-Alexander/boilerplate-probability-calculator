import random
import copy


class Hat:

    def __init__(self, **args):
        self.contents = []
        for color, num_balls in args.items():
            self.contents += [color] * num_balls
    
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num_balls)
        for b in drawn_balls:
            self.contents.remove(b)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for i in range(num_experiments):
        # Make a copy of the hat to avoid modifying the original
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count how many of each color were drawn
        drawn_balls_count = {}
        for ball in drawn_balls:
            drawn_balls_count[ball] = drawn_balls_count.get(ball, 0) + 1

        # Check if we drew the expected number of each color
        all_expected_balls_drawn = True
        for color, num_balls in expected_balls.items():
            if color not in drawn_balls_count or drawn_balls_count[color] < num_balls:
                all_expected_balls_drawn = False
                break
        if all_expected_balls_drawn:
            successful_experiments += 1

    return successful_experiments / num_experiments
