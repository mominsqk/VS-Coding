# Define a function to demonstrate the use of match-case
def describe_number(number):
    # Using 'match' to match the value of 'number' with different cases
    match number:
        # Case 1: if number is 0
        case 0:
            return "Zero"  # Return a string "Zero" if the number is 0
        # Case 2: if number is 1
        case 1:
            return "One"  # Return "One" if the number is 1
        # Case 3: if number is 2
        case 2:
            return "Two"  # Return "Two" if the number is 2
        # Default case: if number is none of the above
        case _:
            return "Unknown"  # Return "Unknown" if no other case matches

# Take input from the user
try:
    user_input = int(input("Enter a number: "))  # Convert input to integer
    # Call the function and print the result
    print(describe_number(user_input))
except ValueError:
    print("Please enter a valid integer.")  # Handle non-integer inputs


# Take input from the user
user_input = input("Enter a color (red, green, blue): ").lower()  # Convert to lowercase to handle case insensitivity

# Using 'match' to match the value of 'user_input' with different cases
match user_input:
    # Case 1: if color is "red"
    case "red":
        print("You chose Red!")  # Output for red
    # Case 2: if color is "green"
    case "green":
        print("You chose Green!")  # Output for green
    # Case 3: if color is "blue"
    case "blue":
        print("You chose Blue!")  # Output for blue
    # Default case: if color is none of the above
    case _:
        print("Unknown color!")  # Output if input doesn't match any case


us_input = input('enter your name: ')
city_input = input('enter city name: ')
if us_input== 'momin':
    if city_input== 'pindi':
        print('you are welcome to islamabad')
if us_input== 'ali':
    if city_input=='pindi':
        print('welcome to multan')
else:
    print('you are not invited yet')




