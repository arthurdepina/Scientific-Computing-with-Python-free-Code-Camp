import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for color, quantity in kwargs.items():
            for i in range(quantity):
                self.contents.append(color)

    def draw(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents
        output = random.sample(self.contents, number_of_balls)
        for i in output:
            self.contents.remove(i)
        return output


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    expected_balls_list = list()
    for color in expected_balls:
        for i in range(expected_balls[color]):
            expected_balls_list.append(color)

    for exp in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        new_expected_balls = copy.deepcopy(expected_balls_list)

        drew = new_hat.draw(num_balls_drawn)

        for ball in drew:
            if ball in new_expected_balls:
                new_expected_balls.remove(ball)

        if len(new_expected_balls) == 0:
            successes += 1

    print(successes)
    return successes/num_experiments
