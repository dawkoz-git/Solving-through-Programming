def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_task1():
    chance = likelihood()
    print(f"Minimum likelihood of falling is {chance}%.")


run_task1()
