def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_task1():
    chance = likelihood()
    print(f"Minimum likelihood of falling is {chance}%.")


# run_task1()

def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run_task2():
    min_max = likelihood_min_max()

    print(f"Minimum likelihood of falling is {min_max[0]}.")
    print(f"Maximum likelihood of falling is {min_max[1]}.")


run_task2()
