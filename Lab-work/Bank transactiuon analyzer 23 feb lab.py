# Sample transaction list (positive = deposit, negative = withdrawal)
transactions = [15000, -5000, 8000, -12000, 25000, -3000, 500]

# Step 1: Calculate total balance
total_balance = sum(transactions)

# Step 2: Find largest withdrawal
withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals) if withdrawals else 0  # most negative value

# Step 3: Count number of deposits greater than 10000
large_deposits_count = sum(1 for t in transactions if t > 10000)

print("Total Balance:", total_balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Number of Deposits > 10,000:", large_deposits_count)