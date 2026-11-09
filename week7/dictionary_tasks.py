def pattern():
    sequence = {"Short sequence": 3, "Medium sequence": 2, "Long sequence": 1}
    return sequence


def display_keys(data):
    for key in data.keys():
        print(key)


def display_values(data):
    for i in data.values():
        print(i)


def display_items(data):
    for i in data.items():
        print(i)


def run():
    data = pattern()
    display_keys(data)
    display_values(data)
    display_items(data)


run()
