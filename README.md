# FINE 3300 - Mortgage Payment Calculator [Assignment #1 Description]

Project Overview

This project calculates mortgage payments for various payment frequencies based on user input. It implements a function that determines the periodic payment amounts for fixed-rate mortgages in Canada. The program uses the present value of an annuity formula and accounts for different compounding periods.

How to Use the Code

Install Python if not already installed.

Clone this repository using Git:

git clone https://github.com/yourusername/FINE3300-Mortgage-Payments.git

Open the project folder in Visual Studio Code or any Python IDE.

Run the script using:

python mortgage_calculator.py

Enter the required inputs when prompted:

Principal Amount (e.g., 500000)

Quoted Interest Rate (%) (e.g., 5.5)

Amortization Period (Years) (e.g., 25)

Inputs & Outputs

Inputs: The user provides the mortgage principal, the quoted annual interest rate, and the amortization period.

Outputs: The program calculates and displays the mortgage payments for different payment schedules:

Monthly

Semi-monthly

Bi-weekly

Weekly

Accelerated Bi-weekly

Accelerated Weekly

Example Output

For a mortgage of $500,000 at an interest rate of 5.5%, amortized over 25 years, the output is:

Monthly Payment: $3,051.94
Semi-monthly Payment: $1,525.97
Bi-weekly Payment: $1,406.92
Weekly Payment: $703.46
Rapid Bi-weekly Payment: $1,525.97
Rapid Weekly Payment: $762.99

GitHub Repository

[Your GitHub Repository Link Here]

Notes

The script assumes valid user inputs.

Payments are rounded to the nearest cent.

The periodic rate is derived based on semi-annual compounding conventions used in Canada.

This project is part of FINE 3300 (Winter 2025) Assignment #1 at [Your University Name].
