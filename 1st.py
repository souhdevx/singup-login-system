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
    find = False
    name2 =  input("Username: ")
    password2 = input("Password: ")
    for user in users:
        if name2 == user["name"] or password2 == user["password"]:
            find = True
            print("Welcome back sir! ")
    if find == False:
        print("Incorrect username or password")    
def change_password():
    find = False
    name = input("Enter you account username: ")
    for user in users:
        if user["name"] == name:
            find = True
            password = input("Enter the curent password: ")
            if user["password"] == password and user["name"] == name:
                new_password = input("Enter your new password: ")
                user["password"] = new_password         
    if find == False:
        print("We couldn't find your account")
def delete_account():
    name3 = input("Enter your username: ")
    for user in users:  
        if name3 == user["name"]:
            print("if you dleted your account you can't login again to your account or recover it!!!!")
            condition = input("are you shur you want to delete your account(yes/no): ")
            if condition == "yes":
                    password3 = input("Enter your account password: ")       
                    if password3 == user["password"] and name3 == user["name"]:
                        users.remove(user)
                        print("Your account was deleted successfully")
                    else:
                        print("Incorrect password! ")    
            elif condition == "no":
                print("You're welcome any time sir :)")
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
    print("3-go back")
    print("-----------------------------------------")    
while True:
    menu()
    chose = int(input("Take a service: "))
    if chose == 1:
        singup()
    elif chose == 2:
        login()
    elif chose == 3:
        while True:
            settings()
            choice = int(input("How we can help you?: "))
            if choice == 1:
                change_password()
            elif choice == 2:
                delete_account()
            elif choice == 3:
                menu()
                break    
            else:
                print("Invaliable service!")
     
    elif chose == 0:
        print("see you :)")
        break    
    else:
        print("this service is invaliable")        
            