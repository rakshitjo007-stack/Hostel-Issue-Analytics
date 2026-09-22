users = {}
def register():
    name = input("Enter your name: ")
    username = input("Create a username: ")
    if username in users:
        print("Username already exists!")
    else:
        users[username] = name
        print("Registration successful!")
        print("Welcome,", name)
        print("Username:", username)
while True:
    print("===== HOSTEL ISSUE PATTERN & ANALYTICS SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        username = input("Enter your username: ")
        if username in users:
            print("Login successful!")
            print("Welcome,", users[username])
        else:
            print("Username not found")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
