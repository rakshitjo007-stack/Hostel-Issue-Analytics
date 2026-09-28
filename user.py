users = {}

users["admin"] = {
    "name": "Hostel Admin",
    "password": "admin123",
    "role": "Admin"
}


def register():

    print("\n===== STUDENT REGISTRATION =====")

    username = input("Enter username: ")

    if username in users:
        print("Username already exists.")
        return

    name = input("Enter your name: ")
    password = input("Enter password: ")

    users[username] = {
        "name": name,
        "password": password,
        "role": "Student"
    }

    print("Registration successful.")


def login():

    print("\n===== LOGIN =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:

        if users[username]["password"] == password:
            print("Login successful.")
            print("Welcome,", users[username]["name"])
            return username

    print("Invalid username or password.")
    return None