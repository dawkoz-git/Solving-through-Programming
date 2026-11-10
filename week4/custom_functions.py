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


# cross_bridge(3)
# cross_bridge(6)

def climb_ladder(steps_left, steps_crossed):
    if steps_left > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


# climb_ladder(5, 2)
# climb_ladder(2, 5)

def display_ladder(steps):
    for i in range(steps):
        print("| |")
        print("***")


def create_ladder():
    steps = int(input("How many steps remain? "))
    display_ladder(steps)


# create_ladder()

def sum_weights(weight_char, weight_inv):
    total_weight = weight_char + weight_inv
    return total_weight


def calc_avg_weight(weight_char, weight_inv):
    avg_weight = sum_weights(weight_char, weight_inv) / 2
    return avg_weight


def run():
    char = int(input("What is the character's weight? (kg)"))
    inv = int(input("What is the inventory's weight? (kg)"))

    avg_sum = input("Do you want the average weight, or the sum weight (average, sum)")
    if avg_sum == "average":
        print(f"The average weight is {calc_avg_weight(char, inv)} kg.")
    else:
        print(f"The sum weight is {sum_weights(char, inv)} kg.")


# run()

def in_ascii(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print(f"| {word} |")
    print("-" * num_dashes)


def lower(word):
    print(f"{word.lower()}")


def upper(word):
    print(f"{word.upper()}")


def reverse(word):
    reversal = ""
    for letter in word:
        reversal = letter + reversal

    print(reversal)


def repeat(word):
    repeats = int(input("How many times to display the word?: "))
    for i in range(repeats):
        if i % 2 == 0:
            print(f"{word.lower()}")
        else:
            print(f"{word.upper()}")


prompt_word = input("Please enter a word: ")

print("Please pick one of the following options:")
print("""
1) Display in a box - display the word in an ASCII art box
2) Display lowercase - display the word in lowercase.
3) Display uppercase - display the word in uppercase. 
4) Display mirrored - display the word in reverse.
5) Repeat - ask the user how many times to display a word, alternate that in upper/lowercase.     
      """)

response = int(input())

if response == 1:
    in_ascii(prompt_word)
elif response == 2:
    lower(prompt_word)
elif response == 3:
    upper(prompt_word)
elif response == 4:
    reverse(prompt_word)
elif response == 5:
    repeat(prompt_word)
else:
    print("Invalid number!")



