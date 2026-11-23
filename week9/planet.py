class Planet:

    def __init__(self):
        self.humans = []
        self.robots = []
        self.name = "planet"

    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self, human):
        self.humans.remove(human)

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        self.robots.remove(robot)

    def __repr__(self):
        return f"planet(name={self.name}, humans={len(self.humans)}, robots={len(self.robots)}"

    def __str__(self):
        return f"planet name is {self.name}, it has {len(self.humans)} humans, and {len(self.robots)} robots."

