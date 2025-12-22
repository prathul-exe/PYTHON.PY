# Is Your Password Secure 🔐?
"""
Hey there this is my second project which I made while my journey of learning python,
this is a username and password checker that takes a username and password and checks 
whether if the username and password is strong.This also reviews the username and password
and shows us what should be added or changed if it is not strong.
---16-12-2025
"""
#👉User Input(username  and password)
print("✅ Creatinng a New Account...")
username=input("Username: ")
password=input("Password: ")
print("-"*50)

def check_password(password):

    print("-"*50)   
    print(f"Checking Password: {password}")

    #📦 Placeholders
    symbols="!@#$%^&*()_-+<>/\?{}|"
    check_length=False
    check_digit=False
    check_lower=False
    check_upper=False
    check_symbol=False
    check_no_spaces=False

    #💪Security Checks

    #✅ Length (minimum 8 characters)
    if len(password)>=8:
        check_length=True

    ##✅ Contains no spaces
    if " " not in password:
        check_no_spaces=True


    for char in password:

        #✅ Contains at least one digit
        if char.isdigit():
            check_digit=True

        #✅ Contains at least one uppercase letter
        elif char.isupper():
            check_upper=True

        #✅ Contains at least one lowercase letter
        elif char.islower():
            check_lower=True
        #✅ Contains at least one special character
        elif char in symbols:
            check_symbol=True
    # Display Results
    checks=[check_length,check_digit,check_lower,check_upper,check_symbol]

    if all(checks):
        print("Password is strong")
    else:
        print("Password is not strong enough⚠️")
        
        if not check_digit:
            print("❌-At least one digit!")
        if not check_length:
            print("❌-At least 8 characters!")
        if not check_symbol:
            print(f"❌-At least one symbol ({symbols})")
        if not check_upper:
            print(f"❌-At least one uppercase letter")
        if not check_lower:
            print(f"❌-At least one lowercase letter")
        if not check_no_spaces:
            print(f"❌-Should contain no spaces!")
def check_username(password):

    print("-"*50)   
    print(f"Checking Username: {username}")

    #📦 Placeholders
    symbols="!@#$%^&*()_-+<>/\?{}|"
    check_length=False
    check_digit=False
    check_lower=False
    check_upper=False
    check_symbol=False
    check_no_spaces=False

    #💪Security Checks

    #✅ Length (minimum 8 characters)
    if len(username)>=8:
        check_length=True

    ##✅ Contains no spaces
    if " " not in username:
        check_no_spaces=True


    for char in username:

        #✅ Contains at least one digit
        if char.isdigit():
            check_digit=True

        #✅ Contains at least one uppercase letter
        elif char.isupper():
            check_upper=True

        #✅ Contains at least one lowercase letter
        elif char.islower():
            check_lower=True
        #✅ Contains at least one special character
        elif char in symbols:
            check_symbol=True
    # Display Results
    checks=[check_length,check_digit,check_lower,check_upper,check_symbol]

    if all(checks):
        print("Username is unique")
    else:
        print("Username is not unique enough⚠️")
        
        if not check_digit:
            print("❌-At least one digit!")
        if not check_length:
            print("❌-At least 8 characters!")
        if not check_symbol:
            print(f"❌-At least one symbol ({symbols})")
        if not check_upper:
            print(f"❌-At least one uppercase letter")
        if not check_lower:
            print(f"❌-At least one lowercase letter")
        if not check_no_spaces:
            print(f"❌-Should contain no spaces!")

#using the function
check_username(username)
check_password(password)
