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


run_task2()
