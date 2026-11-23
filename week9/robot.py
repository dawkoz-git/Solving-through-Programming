class Robot:

    MAX_ENERGY = 100

    def __init__(self, energy=0):
        self.energy = energy

    def display(self):
        print(f"I have {self.energy} energy.")


if __name__ == "__main__":
    robot = Robot()
    robot.display()
