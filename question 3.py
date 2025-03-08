# Question 3

# Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a
# separate line. Ask the user to enter a three-digit number. If the number they have typed in matches one in
# the list, display the position of that number in the list, otherwise display the message “That is not in the
# list”.


# Create a list of four three-digit numbers
numbers_list = [123, 456, 789, 321]

# Display the list, each item on a separate line
print("Here is the list of numbers:")
for num in numbers_list:
    print(num)

# Ask the user to enter a three-digit number
user_number = int(input("\nEnter a three-digit number: "))

# Check if the number is in the list
if user_number in numbers_list:
    # Find the position of the number in the list (indexing starts from 0)
    position = numbers_list.index(user_number)
    print(f"The number {user_number} is at position {position} in the list.")
else:
    print("That is not in the list.")
