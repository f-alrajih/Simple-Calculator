def add_two_numbers(x, y):
  return x + y

def subtract_two_numbers(x, y):
  return x - y

def multiply_two_numbers(x, y):
  return x * y 

def divide_two_numbers(x, y):
  return x/y 

def calculator_menu(): 
  print("Select 1 to add")
  print("Select 2 to subtract")
  print("Select 3 to multiply")
  print("Select 4 to divide")

def greeting_and_directions():
  print("Welcome to Faisal's Simple Calculator!") 
  print("Choose one of the options below, then press enter.")

greeting_and_directions()
calculator_menu()

menu_choice = input("What would you like to do? ")

first_number = input("What is your first number? ")
second_number = input("What is your second number? ")

first_number = int(first_number)
second_number = int(second_number)

if menu_choice == "1":
  print(add_two_numbers(first_number, second_number))

if menu_choice == "2": 
  print(subtract_two_numbers(first_number, second_number))

if menu_choice == "3":
  print(multiply_two_numbers(first_number, second_number))

if menu_choice == "4": 
  print(divide_two_numbers(first_number, second_number))
