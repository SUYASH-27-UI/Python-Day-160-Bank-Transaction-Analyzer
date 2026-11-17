
import csv
from collections import defaultdict

FILE_NAME = "transactions.csv"

income = 0
expenses = 0
category_totals = defaultdict(float)

transactions = []

try:
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["Amount"])
            transaction_type = row["Type"].strip().lower()
            category = row["Category"].strip()

            transactions.append(row)

            if transaction_type == "income":
                income += amount
            elif transaction_type == "expense":
                expenses += amount
                category_totals[category] += amount

    print("\n===== BANK TRANSACTION REPORT =====")
    print("Total Transactions:", len(transactions))
    print(f"Total Income: Rs. {income:.2f}")
    print(f"Total Expenses: Rs. {expenses:.2f}")
    print(f"Remaining Balance: Rs. {income - expenses:.2f}")

    print("\n===== CATEGORY-WISE EXPENSES =====")

    for category, amount in category_totals.items():
        print(f"{category}: Rs. {amount:.2f}")

    if category_totals:
        highest = max(category_totals, key=category_totals.get)
        print("\nHighest Spending Category:", highest)

except FileNotFoundError:
    print("Transaction file not found.")

except (ValueError, KeyError):
    print("Invalid transaction data in CSV file.")
