# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you, {name}!")

print("Please enter a character for the robot' eye.")
eye = input()

print("########")
print(f"# {eye}  {eye} #")
print("# ____ #")
print("########")

print("What is your name?")
newname = input()

print("What is your age?")
age = int(input())

print("What is your height in meters?")
height = float(input())

print("What is your weight in kilograms?")
weight = int(input())

bmi = weight / height ** 2
print(f"{newname}, you are {age} years old and your BMI is {bmi}.")

print("Please enter the number of lives.")
lives = int(input())

print("Please enter the energy levels.")
energy = int(input())

print("Please enter the shield levels.")
shield = int(input())

print("Confirmed.")

print(f"Lives: {lives * '♥'}")
print(f"Energy: {energy * '♦'}")
print(f"Shields: {energy * '♦'}")
