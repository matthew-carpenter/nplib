from numpy import *


def get_gradient_descent(points, starting_b, starting_m, learning_rate, iterations):
    b = starting_b
    m = starting_m
    for i in range(iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]


def get_linear_regression_error(b, m, points):
    total_error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))


def step_gradient(current_b, current_m, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    n = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / n) * (y - ((current_m * x) + current_b))
        m_gradient += (2 / n) * x * (y - ((current_m * x) + current_b))
    new_b = current_b - (learning_rate * b_gradient)
    new_m = current_m - (learning_rate * m_gradient)
    return [new_b, new_m]


def run():
    # Step 1 - collect our data
    points = genfromtxt('data.csv', delimiter=',')

    # Step 2 - define our hyperparameters

    learning_rate = 0.0001  # how fast should our model converge

    # y = mx + b (slope formula)
    initial_b = 0
    initial_m = 0

    iterations = 1000

    # Step 3 - train our model
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m,
                                                                              get_linear_regression_error(initial_b,
                                                                                                          initial_m,
                                                                                                          points))
    [b, m] = get_gradient_descent(points, initial_b, initial_m, learning_rate, iterations)
    print "After 1000 iterations b = {1}, m = {2}, error = {3}".format(iterations, b, m,
                                                                       get_linear_regression_error(b, m, points))


if __name__ == '__main__':
    run()
