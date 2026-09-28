from storage import save_issues, load_issues


issues = load_issues()


def report_issue(username):

    print("\n===== REPORT HOSTEL ISSUE =====")

    room = input("Enter Room Number: ")
    block = input("Enter Hostel Block: ")

    print("\nSelect Issue Category:")
    print("1. Electrical")
    print("2. Plumbing")
    print("3. Cleaning")
    print("4. Furniture")
    print("5. Other")

    category_choice = input("Enter your choice: ")

    if category_choice == "1":
        category = "Electrical"
    elif category_choice == "2":
        category = "Plumbing"
    elif category_choice == "3":
        category = "Cleaning"
    elif category_choice == "4":
        category = "Furniture"
    elif category_choice == "5":
        category = "Other"
    else:
        print("Invalid category.")
        return

    description = input("Enter Description: ")

    print("\nSelect Priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("Enter your choice: ")

    if priority_choice == "1":
        priority = "Low"
    elif priority_choice == "2":
        priority = "Medium"
    elif priority_choice == "3":
        priority = "High"
    else:
        print("Invalid priority.")
        return

    ticket_id = "HIA-" + str(len(issues) + 1)

    issue = {
        "ticket_id": ticket_id,
        "room": room,
        "block": block,
        "category": category,
        "description": description,
        "priority": priority,
        "status": "Pending",
        "reported_by": username
    }

    issues.append(issue)
    save_issues(issues)

    print("\nIssue reported successfully!")
    print("\n===== ISSUE TICKET =====")
    print("Ticket ID:", ticket_id)
    print("Room:", room)
    print("Block:", block)
    print("Category:", category)
    print("Description:", description)
    print("Priority:", priority)
    print("Status: Pending")


def view_issues(username):

    print("\n===== MY ISSUES =====")

    found = False

    for issue in issues:

        if issue["reported_by"] == username:

            found = True

            print("\nTicket ID:", issue["ticket_id"])
            print("Room:", issue["room"])
            print("Block:", issue["block"])
            print("Category:", issue["category"])
            print("Description:", issue["description"])
            print("Priority:", issue["priority"])
            print("Status:", issue["status"])
            print("----------------------------")

    if found == False:
        print("No issues reported yet.")


def view_all_issues():

    if len(issues) == 0:
        print("No issues have been reported yet.")
        return

    print("\n===== ALL HOSTEL ISSUES =====")

    for issue in issues:

        print("\nTicket ID:", issue["ticket_id"])
        print("Reported By:", issue["reported_by"])
        print("Room:", issue["room"])
        print("Block:", issue["block"])
        print("Category:", issue["category"])
        print("Description:", issue["description"])
        print("Priority:", issue["priority"])
        print("Status:", issue["status"])
        print("----------------------------")


def update_issue():

    if len(issues) == 0:
        print("No issues available.")
        return

    ticket_id = input("Enter Ticket ID: ")

    for issue in issues:

        if issue["ticket_id"] == ticket_id:

            print("\nCurrent Status:", issue["status"])

            print("1. Pending")
            print("2. In Progress")
            print("3. Resolved")

            choice = input("Enter new status: ")

            if choice == "1":
                issue["status"] = "Pending"
            elif choice == "2":
                issue["status"] = "In Progress"
            elif choice == "3":
                issue["status"] = "Resolved"
            else:
                print("Invalid choice.")
                return

            save_issues(issues)

            print("Issue status updated successfully.")
            return

    print("Ticket ID not found.")