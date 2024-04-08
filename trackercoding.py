import pickle
from collections import defaultdict
from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, category, amount, date):
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount
        self.date = date

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def enter_expense(self, category, amount, date):
        expense = Transaction("Expense", category, amount, date)
        self.transactions.append(expense)

    def enter_income(self, source, amount, date):
        income = Transaction("Income", source, amount, date)
        self.transactions.append(income)

    def calculate_budget(self):
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.transaction_type == "Income")
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.transaction_type == "Expense")
        remaining_budget = total_income - total_expenses
        return remaining_budget

    def analyze_expenses(self):
        expenses_by_category = defaultdict(float)
        for transaction in self.transactions:
            if transaction.transaction_type == "Expense":
                expenses_by_category[transaction.category] += transaction.amount
        return expenses_by_category

    def save_transactions(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.transactions, file)

    def load_transactions(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.transactions = pickle.load(file)
        except FileNotFoundError:
            pass  # If the file doesn't exist, start with an empty transaction list

# Example usage
budget_tracker = BudgetTracker()

budget_tracker.enter_income("Salary", 5000, datetime.now())
budget_tracker.enter_expense("Food", 200, datetime.now())
budget_tracker.enter_expense("Transportation", 100, datetime.now())

print("Remaining Budget:", budget_tracker.calculate_budget())
print("Expense Analysis:", budget_tracker.analyze_expenses())

budget_tracker.save_transactions("transactions.pkl")

# After restarting the application
budget_tracker = BudgetTracker()
budget_tracker.load_transactions("transactions.pkl")

print("Remaining Budget:", budget_tracker.calculate_budget())
print("Expense Analysis:", budget_tracker.analyze_expenses())
