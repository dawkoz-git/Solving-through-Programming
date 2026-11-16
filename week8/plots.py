import matplotlib.pyplot as plt


def display_line(x, y):
    plt.plot(x, y)
    plt.show()


def run_task1():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)


# run_task1()

def small():
    x_values = [3, 4, 4, 3, 3]
    y_values = [3, 3, 4, 4, 3]

    plt.plot(x_values, y_values, "r:o")


def medium():
    x_values = [2, 5, 5, 2, 2]
    y_values = [2, 2, 5, 5, 2]

    plt.plot(x_values, y_values, "g--s")


def large():
    x_values = [1, 6, 6, 1, 1]
    y_values = [1, 1, 6, 6, 1]

    plt.plot(x_values, y_values, "b-*")


def run_task2():
    small()
    medium()
    large()
    plt.show()


run_task2()
