def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    print(observed())


def observed_items():
    observations = []
    for items in range(7):
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


run_task2()
