from user import register, login, users
from issue import report_issue, view_issues, view_all_issues, update_issue, issues


print("\n===== HOSTEL ISSUE MANAGEMENT SYSTEM =====")


while True:

    print("\n===== MAIN MENU =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        current_user = login()

        if current_user is not None:

            if users[current_user]["role"] == "Student":

                while True:

                    print("\n===== STUDENT MENU =====")
                    print("1. Report Issue")
                    print("2. View Issues")
                    print("3. Logout")

                    student_choice = input("Enter your choice: ")

                    if student_choice == "1":
                        report_issue(current_user)

                    elif student_choice == "2":
                        view_issues(current_user)

                    elif student_choice == "3":
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid choice.")

            elif users[current_user]["role"] == "Admin":

                while True:

                    print("\n===== ADMIN MENU =====")
                    print("1. View All Issues")
                    print("2. Update Issue")
                    print("3. Logout")

                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        view_all_issues()

                    elif admin_choice == "2":
                        update_issue()

                    elif admin_choice == "3":
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid choice.")

    elif choice == "3":
        print("Thank you for using Hostel Issue Management System.")
        break

    else:
        print("Invalid choice.")