# FINE3300 Assignment #1: Mortgage Payment Calculator

This Python program calculates mortgage payments for various payment frequencies, including monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, and rapid weekly. It is designed to help users understand how different payment schedules affect their mortgage payments.

## Features
- **Flexible Inputs**: Users can input the principal amount, annual interest rate, and amortization period.
- **Multiple Payment Frequencies**: The program calculates payments for:
  - Monthly
  - Semi-monthly
  - Bi-weekly
  - Weekly
  - Rapid bi-weekly (accelerated)
  - Rapid weekly (accelerated)
- **Accurate Calculations**: Uses the present value of annuity factor to ensure precise payment amounts.
- **User-Friendly Output**: Displays the results in a clear and easy-to-read format.

## How It Works
1. The program prompts the user to enter:
   - The principal amount (total loan amount).
   - The annual interest rate (as a percentage, e.g., 5.5 for 5.5%).
   - The amortization period (in years).
2. It then calculates the payments for all six payment frequencies using the provided formulas.
3. Finally, it displays the results rounded to the nearest penny.

## Example Output
For a principal of $100,000, an interest rate of 5.5%, and an amortization period of 25 years, the program outputs:

Monthly Payment: $610.39
Semi-monthly Payment: $304.85
Bi-weekly Payment: $281.38
Weekly Payment: $140.61
Rapid Bi-weekly Payment: $305.20
Rapid Weekly Payment: $152.60


## Getting Started
1. Clone this repository to your local machine (such as through "Command Prompt"):
   git clone https://github.com/DanJoh31/FINE3300-Mortgage-Payments.git
2. Navigate to the project folder:
    cd FINE3300-Mortgage-Payments
3. Run the program:
    python mortgage_calculator.py

### Author
Daniel Johannes
[This program was created as part of the FINE3300 course at York University]
