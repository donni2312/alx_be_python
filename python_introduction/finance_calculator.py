"""_summary_
    Instructions:

User Input for Financial Details:

Prompt the user for their monthly income: “Enter your monthly income: ”.
Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
Calculate Monthly Savings:

Calculate the monthly savings by subtracting monthly expenses from the monthly income.
Project Annual Savings:

Assume a simple annual interest rate of 5%.
Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
Output Results:

Display the user’s monthly savings.
Display the projected annual savings after including interest.
Example Interaction:

Enter your monthly income: 5000
Enter your total monthly expenses: 4000
Your monthly savings are $1000.
Projected savings after one year, with interest, is: $12600.
    """
    
# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - total_monthly_expenses

# Project Annual Savings
annual_interest_rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Output Results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
