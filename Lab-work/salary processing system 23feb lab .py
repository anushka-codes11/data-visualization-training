# Salary Processing System

# Example list of employee salaries
salaries = [30000, 55000, 48000, 60000, 25000, 75000, 52000]

# Minimum wage
minimum_wage = 30000

# Step 1: Remove salaries below minimum wage
valid_salaries = [s for s in salaries if s >= minimum_wage]

# Step 2: Add 5% bonus for salaries > 50000
processed_salaries = []
for s in valid_salaries:
    if s > 50000:
        s += s * 0.05  # 5% bonus
    processed_salaries.append(s)

# Step 3: Sort salaries in descending order
processed_salaries.sort(reverse=True)

# Step 4: Display top 3 highest salaries
top_3_salaries = processed_salaries[:3]

# Display results
print("---- Salary Processing ----")
print("Original Salaries:", salaries)
print("Valid Salaries (>= minimum wage):", valid_salaries)
print("Processed Salaries (with bonus if applicable):", processed_salaries)
print("Top 3 Highest Salaries:", top_3_salaries)