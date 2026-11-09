import json


def read(path):
    with open(path) as f:
        data = json.load(f)

        location = data["location"]
        population = data["population"]

        print(f"Place Name: {location}")
        print(f"Population Size: {population}")

        for i in data["bots"]:
            name = i["name"]
            stats = i["stats"]
            print(f"{name} has the following stats: {stats}.")


def run():
    read("futurama.json")


def read_task2(file_path):
    print("Reading...")
    with open(file_path) as f:
        data = json.load(f)
    print("Done!")
    return data


def save(file_path, data_saving):
    print("Exporting...")
    with open(file_path, "w") as f:
        json.dump(data_saving, f, indent=4)
        print("Done!")


def run_task():
    json_data = read_task2("futurama.json")
    save("exported.json", json_data)


run_task()
