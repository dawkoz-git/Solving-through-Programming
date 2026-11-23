class Robot:

    MAX_ENERGY = 100

    def __init__(self, name="Robot", energy=0):
        self.name = name
        self.energy = energy

    def display(self):
        print(f"I have {self.energy} energy.")

    def __repr__(self):
        return f"robot(name={self.name}, energy={self.energy})"

    def __str__(self):
        return f"Robot {self.name} has {self.energy} energy."


if __name__ == "__main__":
    robot = Robot()
    robot.display()
