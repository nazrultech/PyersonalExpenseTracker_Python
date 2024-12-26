import json
from datetime import datetime

expenses = []
budget = {}

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description (optional): ")
    expenses.append({"date": date, "amount": amount, "category": category, "description": description})
    print("Expense added successfully!")

def view_expenses():
    print("\n--- Expenses ---")
    for expense in expenses:
        print(f"{expense['date']}: {expense['amount']} ({expense['category']}) - {expense['description']}")

def set_budget():
    global budget
    budget = {}
    print("Set monthly budget for categories. Type 'done' to finish.")
    while True:
        category = input("Enter category: ")
        if category.lower() == 'done':
            break
        amount = float(input(f"Enter budget for {category}: "))
        budget[category] = amount
    total_budget = float(input("Enter total monthly budget: "))
    budget["Total"] = total_budget
    print("Budget set successfully!")

def view_budget_status():
    print("\n--- Budget Status ---")
    category_totals = {cat: 0 for cat in budget if cat != "Total"}
    total_spent = 0
    for expense in expenses:
        if expense['category'] in category_totals:
            category_totals[expense['category']] += expense['amount']
        total_spent += expense['amount']
    for category, spent in category_totals.items():
        print(f"{category}: Spent {spent}, Remaining {budget[category] - spent}")
    print(f"Total: Spent {total_spent}, Remaining {budget['Total'] - total_spent}")

def save_to_file():
    with open("D:\\IITM\\IITM AG\\Python Fundamentals\\Python_Project\\expenses.json", "w") as file:
        json.dump({"expenses": expenses, "budget": budget}, file)
    print("Data saved successfully!")

def load_from_file():
    global expenses, budget
    try:
        with open("D:\\IITM\\IITM AG\\Python Fundamentals\\Python_Project\\expenses.json", "r") as file:
            data = json.load(file)
            expenses = data["expenses"]
            budget = data["budget"]
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No saved data found.")

def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Monthly Budget")
        print("4. View Budget Status")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            view_budget_status()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

