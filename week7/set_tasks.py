def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    print(observed())


def observed_items():
    observations = []
    for items in range(5):
        observations.append(input("Please enter your observation: "))
    return observations


def run_task2():
    print("Counting observations...")
    observations = observed_items()

    observations_set = set()
    for i in observations:
        data = (i, observations.count(i))
        observations_set.add(data)

    for let, dig in observations_set:
        print(f"{let} has been observed {dig} time(s).")


def remove_observations(observations):
    print("Do you wish to remove an observation?")
    answer = input("Yes or no?")

    while answer == "yes":
        removal = input("What observation would you like to remove?")
        observations.remove(removal)
        print("All done!")
        answer = input("Would you like to remove another?")


def run_task3():
    observations = observed_items()
    remove_observations(observations)

    observation_set = set()
    for i in observations:
        tup = (i, observations.count(i))
        observation_set.add(tup)

    for i in sorted(observation_set):
        print(f"{i[0]} has been observed {i[1]} time(s).")


run_task3()
