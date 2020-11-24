# Welcome, Faisal, to your first project in Python!

# Today's project is to build a simple calculator that allows the user to choose what type of operation they want to do (add, subtract, multiply, or divide) and then takes the two numbers the user gives it and does the operation.

# You will need to build four different functions for this assignment:

# 1. A function called add_two_numbers with inputs x and y. The function returns the sum of those two numbers. 

# 2. A function called subract_two_numbers with inputs x and y. The function returns the difference of those two numbers.

# 3. A function called multiply_two_numbers with inputs x and y. The function returns the product of those two numbers.

# 4. A function called divide_two_numbers with inputs x and y. The function returns the quotient of those two numbers.

# Once you finish these four functions and test them, come to me and I'll give you more directions!

# -------------

# Great! You're ready to move on to creating a menu for the user to select from.

# Create a function called calculator_menu that prints four different strings:
# "Select 1 to add"
# "Select 2 to subtract"
# "Select 3 to multiply"
# "Select 4 to divide"

# Test the calculator_menu() by calling it.

# -------------

# Great! We wrote our menu. But, we need some directions for the user to follow. 

# Create a function called greeting_and_directions that prints a greeting and directions for the menu:

# "Welcome to Faisal's Simple Calculator!"
# "Choose one of the options below, then press enter."

# -------------

# Awesome! We're so close!

# Now, we need some kind of way to get the user's answer to our directions so that we know what kind of operation to do. This is called user input.

# Create a variable called menu_choice that takes the user's input when asked "What would you like to do?"

# -------------

# Cool! Let's create two more variables, first_number and second_number, that ask the user for their first and second numbers.

# -------------

# Looking awesome! Let's create a conditional that figures what operation to do based on the user's menu choice.

# If menu_choice equals 1, call add_two_numbers()
# If menu_choice equals 2, call subtract_two_numbers()
# If menu_choice equals 3, call multiply_two_numbers()
# If menu_choice equals 4, call divide_two_numbers()

# ----------

# Okay, so it looks like we have two problems: we can't see the menu and the greeting, and we can't see the answer. Let's fix that.

# Call greeting_and_directions() and calculator_menu() above where you define menu_choice.

# -----------

# Great! We can see the greeting and menu, but we still can't see the answer.

# Go to your conditional statements where you checked for the value of menu choice. Print whatever add_two_numbers(), subtract_two_numbers(), multiply_two_numbers(), and divide_two_numbers() returns.
