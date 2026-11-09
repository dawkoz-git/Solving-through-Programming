def short_pattern():
    pattern = {"sequence": "101", "occurences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurences": 50}
    return pattern


def run_task():

    print("Analysing patterns...")
    patterns = {
        "short_pattern": short_pattern(),
        "medium_pattern": medium_pattern(),
        "long_pattern": long_pattern(),
    }

    for key, value in patterns.items():
        print(f"{key}: {value}")


run_task()


