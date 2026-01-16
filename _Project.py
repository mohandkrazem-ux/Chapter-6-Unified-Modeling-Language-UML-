# Student Course Registration System
# Simple Python Project

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    file = open("users.txt", "a")
    file.write(username + "," + password + "\n")
    file.close()

    print("Registration successful!\n")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    file = open("users.txt", "r")
    users = file.readlines()
    file.close()

    for user in users:
        saved_username, saved_password = user.strip().split(",")
        if username == saved_username and password == saved_password:
            print("Login successful!\n")
            return

    print("Invalid username or password.\n")


while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")
