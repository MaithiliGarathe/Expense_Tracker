import csv
import os
from datetime import date

# File jahan expenses save hongi
FILE_NAME = "expenses.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    print("\n💰 Naya Expense Add Karo")
    category = input("Category (Food/Travel/Shopping/Other): ")
    amount = float(input("Amount (Rs): "))
    description = input("Description: ")
    today = str(date.today())

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, category, amount, description])
    print(f"✅ Rs.{amount} ka expense add ho gaya!")

def view_expenses():
    print("\n📊 Tumhare Saare Expenses:")
    print("=" * 50)
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Header skip karo
        expenses = list(reader)

    if len(expenses) == 0:
        print("Koi expense nahi hai abhi!")
    else:
        for i, row in enumerate(expenses, 1):
            print(f"{i}. {row[0]} | {row[1]} | Rs.{row[2]} | {row[3]}")
            total += float(row[2])
        print("=" * 50)
        print(f"💰 Total Expenses: Rs.{total}")

def view_by_category():
    category = input("\nKaunsi category dekhni hai? (Food/Travel/Shopping/Other): ")
    print(f"\n📊 {category} ke Expenses:")
    print("=" * 50)
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1].lower() == category.lower():
                print(f"{row[0]} | Rs.{row[2]} | {row[3]}")
                total += float(row[2])

    print("=" * 50)
    print(f"💰 {category} Total: Rs.{total}")

def expense_app():
    create_file()
    print("=" * 50)
    print("   💰 Expense Tracker App!")
    print("=" * 50)

    while True:
        print("\nKya karna hai?")
        print("1. Expense add karo")
        print("2. Saare expenses dekho")
        print("3. Category wise dekho")
        print("4. Exit")

        choice = input("\nOption choose karo (1/2/3/4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            print("Bye! 👋")
            break
        else:
            print("❌ Galat option!")

expense_app()