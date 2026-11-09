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


identify()
