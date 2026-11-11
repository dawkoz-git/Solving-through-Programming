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


# run_task2()

def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run_task3():
    likelihoods = steps()
    good_steps = []
    bad_steps = []

    for step in likelihoods:
        if step[1] >= 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)

    print(f"Good steps: {len(good_steps)}. Bad steps: {len(bad_steps)}.")


run_task3()
