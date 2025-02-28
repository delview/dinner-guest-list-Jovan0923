# Create functions
# Function to add people to the list
def add_guest(dinner_list, person):
    dinner_list.append(person)
    return dinner_list
# Function to remove people from the list
def remove_guest(dinner_list, person):
    dinner_list.remove(person)
    return dinner_list
# Greet user
print("Welcome to the dinner invitation generator.")
# Ask for amount of people
amount = int(input("How many people are you inviting to dinner? "))
# Ask for names
names = []
# Make invitation and loop for the amount of people
for i in range(amount):
    name = input("Enter the name of the person you are inviting: ")
    names.append(name)


# Print invitations
for name in names:
    print(f"Hello, {name}. You are invited to dinner at Slumpy Joes please let me know if you can arive.")
# Ask user if they would like to add, remove, or end the genorator
while True:
    action = input("Would you like to [a]dd, [r]emove, or [e]nd the generator? ")
    # Create input for adding people
    if action == "a":
        person = input("Who would you like to add? ")
        add_guest(names, person)
        print(f"{person} has been added to the list.")
        for name in names:
            print(f"Hello, {name}. You are invited to dinner at Slumpy Joes please let me know if you can arrive.")
    # Create input for removing people
    elif action == "r":
        person = input("Who would you like to remove? ")
        remove_guest(names, person)
        print(f"{person} has been removed from the list.")
        for name in names:
            print(f"Hello, {name}. You are invited to dinner at Slumpy Joes please let me know if you can arrive.")
    # Greet user goodbye
    elif action == "e":
        print("Goodbye.")
        break
    else:
        print("Invalid input. Please try again.")







