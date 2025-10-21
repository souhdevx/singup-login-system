import random
users = []

def signup():
    name1 = input("Username: ").strip()
    if not name1:
        print("Username cannot be empty.")
        return
    # prevent duplicate usernames
    for u in users:
        if u["name"] == name1:
            print("Username already exists.")
            return
    password1 = input("Password: ").strip()
    if not password1:
        print("Password cannot be empty.")
        return
    user = {
        "name": name1,
        "password": password1,
    }
    users.append(user)
    print("Signup successful.")

def login():
    name2 = input("Username: ").strip()
    password2 = input("Password: ").strip()
    for user in users:
        # require both username and password to match
        if name2 == user["name"] and password2 == user["password"]:
            print("Welcome back!")
            return
    print("Incorrect username or password.")

def change_password():
    name = input("Enter your account username: ").strip()
    for user in users:
        if user["name"] == name:
            current = input("Enter the current password: ").strip()
            if user["password"] == current:
                new_password = input("Enter your new password: ").strip()
                if new_password:
                    user["password"] = new_password
                    print("Password updated successfully.")
                else:
                    print("New password cannot be empty.")
            else:
                print("Incorrect current password.")
            return
    print("We couldn't find your account.")

def delete_account():
    name3 = input("Enter your username: ").strip()
    for user in users:
        if name3 == user["name"]:
            print("If you delete your account you won't be able to recover it.")
            condition = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
            if condition == "yes":
                password3 = input("Enter your account password: ").strip()
                if password3 == user["password"]:
                    users.remove(user)
                    print("Your account was deleted successfully.")
                else:
                    print("Incorrect password.")
            elif condition == "no":
                print("Account not deleted.")
            else:
                print("Cancelled.")
            return
    print("We couldn't find your account.")

# general program
def menu():
    print("-----------------------------------------")
    print("1 - signup")
    print("2 - login")
    print("3 - settings")
    print("0 - close")
    print("-----------------------------------------")

def settings():
    print("-----------------------------------------")
    print("1 - change password")
    print("2 - delete account")
    print("3 - go back")
    print("-----------------------------------------")

while True:
    menu()
    try:
        chose = int(input("Take a service: ").strip())
    except ValueError:
        print("Please enter a number.")
        continue

    if chose == 1:
        signup()
    elif chose == 2:
        login()
    elif chose == 3:
        while True:
            settings()
            try:
                choice = int(input("How can we help you?: ").strip())
            except ValueError:
                print("Please enter a number.")
                continue
            if choice == 1:
                change_password()
            elif choice == 2:
                delete_account()
            elif choice == 3:
                break
            else:
                print("Invalid service.")
    elif chose == 0:
        print("See you :)")
        break
    else:
        print("This service is unavailable.")
