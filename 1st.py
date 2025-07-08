import random
users = []
def singup():
    name1 = input("Username: ")
    password1 = input("Password: ")
    user = {
        "name": name1,
        "password": password1,
    }
    users.append(user)

def login():
    for user in users:
        while True:
            name2 =  input("Username: ")
            password2 = input("Password: ")
            if name2 != user["name"] or password2 != user["password"]:
                print("Incorrect username or password") 
            else:
                print("Welcome back sir! ")
                break

def change_password():
    while True:
        #2FA code generator
        pin_lenght = 6
        pin = "".join(str(random.randint(0,9))for _ in range(pin_lenght))
        name = input("Enter your account username: ")
        for user in users:
            if name == user["name"]:
                print(f"Your 2FA code is: {pin}")
                twoFA_code = int(input("Enter the code that we send: "))
                while True:
                    if twoFA_code != pin:
                        pin = "".join(str(random.randint(0,9))for _ in range(pin_lenght))
                        print("Incorrect code! ")
                        print(f"Your new 2FA code is: {pin}")
                        twoFA_code = int(input("Enter the code that we send: "))    
                    elif twoFA_code == pin: #create the new password
                        newpassword = ("Enter the new password: ")
                        for user in users:
                            user["password"] = newpassword
                            break                
            else:
                print("We couldn't find your account! ")
def delete_account():
    for user in users:
        name3 = input("Enter your username: ")
        if name3 == user["name"]:
            print("if you dleted your account you can't login again to your account or recover it!!!!")
            condition = input("are you shur you want to delete your account(yes/no): ")
            while True:
                if condition == "yes":
                    password3 = input("Enter your account password: ")       
                    if password3 == user["password"]:
                        users.remove(user)
                    else:
                        print("Incorrect password! ")    
                elif condition == "no":
                    break
        else:
            print("We couldn't find your account! ")              
#general programme
def menu():
    print("-----------------------------------------")
    print("1-signup:")
    print("2-login")
    print("3-settings")
    print("0-close")
    print("-----------------------------------------")
def settings():
    print("-----------------------------------------")
    print("1-change password")
    print("2-delete account")
    print("-----------------------------------------")    
while True:
    menu()
    chose = int(input("Take a service: "))
    if chose == 1:
        singup()
    elif chose == 2:
        login()
    elif chose == 3:
        settings()
        while True:
            choice = int(input("How we can help you?: "))
            if choice == 1:
                change_password()
            elif choice == 2:
                delete_account()
            else:
                print("sorry!")
                break           
    elif chose == 0:
        print("see you :)")
        break    
    else:
        print("this service is invaliable")        
            