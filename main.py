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

# Ask user if they would like to add, remove, or end the genorator

# Create input for adding people

# Create input for removing people

# Greet user goodbye


