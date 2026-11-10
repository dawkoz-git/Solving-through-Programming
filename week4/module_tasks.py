import random


def guess_the_number():
    min_val = int(input("Please enter the minimum value: "))
    max_val = int(input("Please enter the maximum value: "))

    ran_num = random.randint(min_val, max_val + 1)

    not_found = True

    print(f"I am thinking of a number between {min_val} and {max_val}. Can you guess what it is?")

    while not_found:
        guess = int(input())

        if guess < ran_num:
            print("Guess is too low! Try again.")
        elif guess > ran_num:
            print("Guess is too high! Try again.")
        elif guess == ran_num:
            print("Your guess is correct! Well done!")
            not_found = not not_found
        else:
            print("Invalid guess! Stay in bounds!")


# guess_the_number()
