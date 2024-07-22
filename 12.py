##username

reserved_words = ['admin', 'root','user']
username = input("Enter username: ")
username_reserved_words = username.lower() in reserved_words
username_lenght = (5 <= len(username) <= 20)
username_alphanumeric = username.isalnum()
if not username_lenght and username_alphanumeric:
    print("username must contain min 5, max 20 symbols(numbers or letters) ")
if username_reserved_words:
    print("username should not be reserved name (e.g., ‘admin’, ‘root’, etc.)")

##email

email = input("Enter vaild email: ")
email_lenght = len(email)!= 2
email_contains_at = "@" in email
email_contains_dot = "." in email
if (email_contains_at and email_contains_dot and email_lenght):
    print("ok")
else:
    print("please enter valid email (e.g., user@example.com)")

##phone number

phone_number = input("Enter valid phone number: ")
phone_number_plus = "+" in phone_number[0]
phone_number_zero = "0" in phone_number[0]
phone_number_digit = phone_number[1:].isdigit()
if ((phone_number_plus or phone_number_zero) and phone_number_digit):
    print("ok")
else:
    print("please enter valid phone number (e.g.,+37499123456 or 099123456)")

##password

password = input("Password should be at least 8 characters long and must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (e.g., !@#$%^&*).\n Enter password: ")
special_characters = "!@#$%^&*?"
password_lenght = (len(password) >= 8)
password_upper = False
password_lower = False
password_digit = False
password_special = False

for letter in password:
    if letter == letter.upper() and not (letter.isdigit() or (letter in special_characters)):
        password_upper = True
for letter in password:
    if letter == letter.lower() and not (letter.isdigit() or (letter in special_characters)):
        password_lower = True
for letter in password:
    if letter.isdigit():
        password_digit = True
for letter in password:
    if letter in special_characters:
        password_special = True
 
if not password_lenght:
    print("password must contain min 8 charachters")

if (password_upper and password_lower) and (password_digit and password_special):
    print("")
else:
    print("password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (e.g., !@#$%^&*)")

##password repeat

password_repeat = input("Repeat password: ")
if password_repeat != password:
    print("Passwords does not match")
else:
    print("success")
