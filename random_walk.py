from random import choice

class RandomWalk:
    """ Points Generator Class"""

    def __init__(self, total_p=5000):
        """ Initializing the arrays and the total of points"""
        self.total = total_p

        self.x_values = [0]
        self.y_values = [0]

    def run_walk(self):

        while len(self.x_values) < self.total:

            direction1 = choice([1, -1])
            length1 = choice([1, 2, 3, 4, 5, 6])
            x_move = direction1 * length1

            direction2 = choice([1, -1])
            length2 = choice([1, 2, 3, 4, 5, 6])
            y_move = direction2 * length2

            x_move = self.x_values[-1] + x_move
            y_move = self.y_values[-1] + y_move

            self.x_values.append(x_move)
            self.y_values.append(y_move)
