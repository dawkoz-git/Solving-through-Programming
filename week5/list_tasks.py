def directions():
    steps = ["Move forward", "Move backward", "Move left", "Move right"]
    return steps


def run_task1():
    print(f"{directions()}")


# run_task1()

def movements():
    path = ["Move forward", 10, "Move Backward", 5, "Move left", 3, "Move right", 1]
    return path


def run_task2():
    print("Moving...")
    movement = movements()

    print(f"{movement[0]} for {movement[1]} steps.")
    print(f"{movement[2]} for {movement[3]} steps.")
    print(f"{movement[4]} for {movement[5]} steps.")
    print(f"{movement[6]} for {movement[7]} steps.")


# run_task2()

def menu():
    print("Please select a direction.")
    direction = directions()

    for i in range(len(direction)):
        print(f"{i}: {direction[i]}")


def run_task3():
    menu()


# run_task3()

def menu_and_input():
    print("Please select a direction.")
    dirs = directions()

    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")

    response = int(input())

    return dirs[response]


def run_task4():
    route = []
    print("Working out escape loop...")

    for i in range(5):
        route.append(menu_and_input())

    print(f"Escape route is {route}.")


run_task4()
