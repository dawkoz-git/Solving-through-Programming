class Human:

    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}.")

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount
        if self.energy + amount > 100:
            self.energy = human.MAX_ENERGY

    def move(self, distance):
        self.energy -= distance
        if self.energy - distance < 0:
            self.energy = 0

    def __repr__(self):
        return f"human(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"human {self.name} is {self.age} and has {self.energy} energy."


if __name__ == "__main__":
    human = Human()
    human.grow()
    human.eat(10)
    human.move(10)
    print(repr(human))
