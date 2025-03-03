# Create functions
# Function to add people to the list
def add_guest(dinner_list, person):# This function will add a person to the list
    dinner_list.append(person)# This will append the person to the list
    return dinner_list# This will return the list
# Function to remove people from the list
def remove_guest(dinner_list, person):# This function will remove a person from the list
    try:
        dinner_list.remove(person)# This will remove the person from the list
        return True
    except ValueError:# This will return an error if the person is not on the list
        (print(f"{person} is not on the list. Please remove someone on the list.")) 
        return False
# Greet user
print("Welcome to the dinner invitation generator.")# This will greet the user
# Ask for amount of people
while True:
    try:
        amount = int(input("How many people are you inviting to dinner? "))
        break
    except ValueError:
        print("Please enter a number.")# This will print if the user enters an invalid input
names = []
# Make invitation and loop for the amount of people
for i in range(amount):# This will loop for the amount of people
    name = input("Enter the name of the person you are inviting: ").strip().title()# This will ask for the name of the person
    names.append(name)


# Print invitations
for name in names:# This will loop for the amount of people so that the invitation will be printed for each person
    print(f"Hello, {name}. You are invited to dinner at Slumpy Joes please let me know if you can arive.")
# Ask user if they would like to add, remove, or end the genorator
while True:
    action = input("Would you like to [a]dd, [r]emove, or [e]nd the generator? ")
    # Create input for adding people
    if action == "a":# This input will check if if the user pressed "a"
        person = input("Who would you like to add? ").strip().title()
        add_guest(names, person)# This will add the person to the list
        print(f"{person} has been added to the list.")# This will print that the person has been added to the list
        for name in names:# This will loop for the amount of people so that the invitation will be printed for each person
            print(f"Hello, {name}. You are invited to dinner at Slumpy Joes please let me know if you can arrive.")# This will print the invitation for each person
    # Create input for removing people
    elif action == "r":# This input will check if if the user pressed "r"
        person = input("Who would you like to remove? ").strip().title()# This will ask for the name of the person
        if remove_guest(names, person):# This will remove the person from the list
            print(f"{person} has been removed from the list.")# This will print that the person has been removed from the list
        for name in names:# This will loop for the amount of people so that the invitation will be printed for each person
            print(f"Hello, {name}. You are invited to dinner at Slumpy Joes please let me know if you can arrive.")# This will print the invitation for each person
    # Greet user goodbye
    elif action == "e":# This input will check if if the user pressed "e"
        print("You may copy and paste the list of names above,")
        break
    else:
        print("Invalid input. Please try again.")# This will print if the user inputs an invalid input







