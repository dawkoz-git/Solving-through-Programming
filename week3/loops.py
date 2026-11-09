
sequence = input("Please enter a sequence. ")
marker = input("Please enter the character for the marker.")

counting = True
counter = 0

for char in sequence:
    if char == marker:
        counting = not counting

    if char != marker:
        counter += 1

print(f"The distance between markers is {counter}.")
