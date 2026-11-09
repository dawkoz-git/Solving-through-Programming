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


if __name__ == "__main__":
    run()
