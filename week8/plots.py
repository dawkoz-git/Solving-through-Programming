import matplotlib.pyplot as plt
import random


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


# run_task2()

def coordinate():
    x = int(input("Please enter an X value (int)."))
    y = int(input("Please enter a Y value (int)."))
    return x, y


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]


def run_task3():
    values = path()
    plt.labels = "x values", "y values"
    plt.plot(values[0], values[1], "r--o")
    plt.show()


# run_task3()

def data():
    paths = {}
    print("What type of line would you like? (:, --, or -)")
    line_type = input()

    print("What color would you like? (r, g, or b)")
    color = input()

    print("What style of marker would you like? (o, s, or ^)")
    style = input()

    paths["Line type"] = line_type
    paths["Color"] = color
    paths["Style"] = style

    return paths


def generate():
    no_of_lines = int(input("How many lines would you like to display?: "))

    for i in range(no_of_lines):
        values = data()
        x = random.randint(1, 100)
        y = random.randint(1, 100)

        plt.plot(x, y, values)
        plt.show()


def run_task4():
    print("Running...")
    generate()
    print("Done!")


run_task4()
