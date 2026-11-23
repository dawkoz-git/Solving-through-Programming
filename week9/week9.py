from planet import Planet
from human import Human

p1 = Planet()

h1 = Human()
h2 = Human()

p1.add_human(h1)
p1.add_human(h2)

print(p1.humans[0].name)

print(repr(p1))