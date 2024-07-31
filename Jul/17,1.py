#task 1: Create a function to greet a user with their full name and a custom message.
# Use positional arguments for first name and last name.
# Use a keyword argument for the greeting message with a default value.

def user_greeting(name, last_name, greeting = "Welcome, dear "):
    
    return f"{greeting} {name} {last_name}"

user_name = input("Enter your name: ")
user_last_name = input("Enter your last name: ")
full_name=(user_name, user_last_name)
print(user_greeting(*full_name))

#taks 2: Write a function to calculate the total price of items in a shopping cart.
# Use positional-only arguments for item prices.
# Use a keyword argument for the tax rate with a default value.
# Return the total price including tax.

def total_price(item1,item2,/, tax_rate = 0.2):
    price = (item1 + item1 * tax_rate) + (item2 + item2 * tax_rate)
    return price
print((f"Total price for items including tax is {total_price(200,300)}"))

#task 3: Create a function to print a user profile.
# Use keyword-only arguments for age and city.
# Use positional arguments for first name and last name. (print_user_profile("John", "Doe", age=30, city="New York")
# Return the result of the operation.

def print_user_profile(name, last_name, *, age, city):
    return f"My name is {name} {last_name}, I'm {age}, i live in {city}."

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(print_user_profile(name, last_name, age = age ,city = f"{city}"))

# #task 4: Write a function to process data with different operations.
# Use positional-only arguments for data (list of numbers).
# Use a keyword argument for the operation (default is ‘sum’).
# Return the result of the operation.

def operator(num1,num2,num3,num4, /,operation = sum):
    list = [num1,num2, num3, num4]
    res = operation(list)
    return res
print(operator(1,2,3,4, operation=max))


# #task 5: Write a function to display product details by unpacking a dictionary.
# Use unpacking to pass product details as keyword arguments to the function.

def product_details(name = "orange", color = "orange", calories = 100, price = "3$"):
    return f" The {name} is {color}, it has {calories} calories, and 1kg costs {price}."

product = {"name" : "apple", "color" : "green", "calories" : "95"}

print(product_details(**product))

# # task 5: Create a function to generate a report with both required and optional sections.
# Use positional arguments for required sections.
# Use keyword arguments for optional sections with default values.

def func(name , last_name, country, age = " "):
    if age == " ":
        return f"My name is {name} {last_name}, i live in {country}"
    return f"My name is {name} {last_name}, i'm {age}, i live in {country}."

print(func("Joe", "Smith", "Armenia", 18))
    