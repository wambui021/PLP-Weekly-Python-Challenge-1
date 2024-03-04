# Create an empty dictionary to store information about a person
person_info = {}

# Ask the user for input and store information in the dictionary
person_info['name'] = input("Enter the person's name: ")
person_info['age'] = input("Enter the person's age: ")
person_info['favorite_color'] = input("Enter the person's favorite color: ")
person_info['hobby'] = input("Enter the person's hobby: ")

# Print the dictionary to the console
print("Person Information:")
for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")
