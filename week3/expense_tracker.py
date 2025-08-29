import csv
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
EXPENSE_FILE = "expenses.csv"
# Step 1: Create CSV if not exists
if not os.path.exists(EXPENSE_FILE):
    with open(EXPENSE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
# Add expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
        category = input("Enter category (Food, Travel, etc.): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        with open(EXPENSE_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
        print(f"Expense of {amount} added successfully!")
    except ValueError:
        print("Invalid input. Amount must be a number.")
    except Exception as e:
        print(f"Error: {e}")
# View expenses
def view_expenses():
    try:
        data = pd.read_csv(EXPENSE_FILE)
        if data.empty:
            print("No expenses found.")
            return
        print("\nYour Expenses:")
        for i, row in data.iterrows():
            print(f"{i+1}. Date: {row['Date']}, Category: {row['Category']}, Amount: {row['Amount']}, Description: {row['Description']}")
        total = data['Amount'].sum()
        print(f"\nTotal Expenses: {total}")
        # Plot expenses by category
        plt.figure(figsize=(8,5))
        sns.barplot(x='Category', y='Amount', data=data, estimator=sum, ci=None, palette='pastel')
        plt.title("Total Expenses by Category")
        plt.show()
        # Plot expenses over time
        data['Date'] = pd.to_datetime(data['Date'])
        daily_expenses = data.groupby('Date')['Amount'].sum().reset_index()
        plt.figure(figsize=(8,5))
        sns.lineplot(x='Date', y='Amount', data=daily_expenses, marker='o')
        plt.title("Daily Expenses Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
def delete_expense():
    try:
        data = pd.read_csv(EXPENSE_FILE)
        if data.empty:
            print("No expenses to delete.")
            return
        view_expenses()
        num = int(input("\nEnter expense number to delete: "))
        if 1 <= num <= len(data):
            removed = data.iloc[num-1]
            data = data.drop(num-1)
            data.to_csv(EXPENSE_FILE, index=False)
            print(f"Expense '{removed['Description']}' deleted successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Enter a number.")
    except Exception as e:
        print(f"Error: {e}")
def show_menu():
    print("\n===== ENHANCED EXPENSE TRACKER MENU =====")
    print("1. Add Expense")
    print("2. View Expenses and Graphs")
    print("3. Delete Expense")
    print("4. Exit")
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")