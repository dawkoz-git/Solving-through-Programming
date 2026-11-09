def listen():
    sound = input("What did you hear? ")
    print(f"That was a loud {sound}!")


# listen()

def identify():
    sight = input("What did you see? ")

    if sight == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")


# identify()

def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big.")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast.")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go.")
    else:
        print("We cannot escape that way! The boulder is in the way.")


# escape_by("jumping over")
# escape_by("running around")
# escape_by("cross bridge ahead")

def cross_bridge(distance_steps):
    for step in range(distance_steps):
        print("Crossed step.")

    if distance_steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")


cross_bridge(3)
cross_bridge(6)
