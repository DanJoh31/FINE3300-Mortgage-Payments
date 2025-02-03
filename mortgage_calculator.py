# FINE3300 Assignment #1 - Mortgage Payment Calculator [By: Daniel Johannes]

# Part 1: Function to calculate mortgage payments
def mortgage_payments(principal, rate, amortization):
    """
    Calculating mortgage payments for various payment frequencies.
    
    Parameters:
    principal (float): The loan amount.
    rate (float): The quoted interest rate (as a percent).
    amortization (int): The amortization period in years.
    
    Returns:
    tuple: A tuple containing monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, and rapid weekly payments.
    """
    # This is to convert quoted rate to decimal and calculate periodic rates
    rq = rate / 100
    r_monthly = (1 + rq / 2) ** (2 / 12) - 1  # Monthly periodic rate
    r_semi_monthly = (1 + rq / 2) ** (2 / 24) - 1  # Semi-monthly periodic rate
    r_bi_weekly = (1 + rq / 2) ** (2 / 26) - 1  # Bi-weekly periodic rate
    r_weekly = (1 + rq / 2) ** (2 / 52) - 1  # Weekly periodic rate

    # This is to calculate number of periods
    n_monthly = amortization * 12  # Total number of monthly payments
    n_semi_monthly = amortization * 24  # Total number of semi-monthly payments
    n_bi_weekly = amortization * 26  # Total number of bi-weekly payments
    n_weekly = amortization * 52  # Total number of weekly payments

    # Present Value of Annuity Factor (PVA)
    def pva(r, n):
        """
        Calculating the present value of annuity factor.
        
        Parameters:
        r (float): Periodic interest rate.
        n (int): Number of periods.
        
        Returns:
        float: Present value of annuity factor.
        """
        return (1 - (1 + r) ** -n) / r

    # Calculating payments
    monthly_payment = principal / pva(r_monthly, n_monthly)  # Monthly payment
    semi_monthly_payment = principal / pva(r_semi_monthly, n_semi_monthly)  # Semi-monthly payment
    bi_weekly_payment = principal / pva(r_bi_weekly, n_bi_weekly)  # Bi-weekly payment
    weekly_payment = principal / pva(r_weekly, n_weekly)  # Weekly payment
    rapid_bi_weekly_payment = monthly_payment / 2  # Rapid bi-weekly payment
    rapid_weekly_payment = monthly_payment / 4  # Rapid weekly payment

    # Returning the payments rounded to the nearest penny
    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(bi_weekly_payment, 2),
        round(weekly_payment, 2),
        round(rapid_bi_weekly_payment, 2),
        round(rapid_weekly_payment, 2)
    )

# Part 2: Prompting the user for input
principal = float(input("Enter the principal amount: "))  # Get principal amount from user
rate = float(input("Enter the quoted interest rate (as a percent, e.g., 7.8% means you should input: 7.8): "))  # Get interest rate from user
amortization = int(input("Enter the amortization period in years: "))  # Get amortization period from user

# Part 3: Calculating and displaying payments
payments = mortgage_payments(principal, rate, amortization)  # Calculate payments
print(f"\nMonthly Payment: ${payments[0]:.2f}")  # Display monthly payment
print(f"Semi-monthly Payment: ${payments[1]:.2f}")  # Display semi-monthly payment
print(f"Bi-weekly Payment: ${payments[2]:.2f}")  # Display bi-weekly payment
print(f"Weekly Payment: ${payments[3]:.2f}")  # Display weekly payment
print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")  # Display rapid bi-weekly payment
print(f"Rapid Weekly Payment: ${payments[5]:.2f}")  # Display rapid weekly payment