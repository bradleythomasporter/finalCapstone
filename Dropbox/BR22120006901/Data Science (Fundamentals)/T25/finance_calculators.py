import math

print("Enter either 'investment' or 'bond' from the menu below to proceed:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")


user_choice = input().lower()


if user_choice not in ["investment", "bond"]:
    print("Invalid input. Please choose either 'investment' or 'bond'.")

elif user_choice == "investment":

    amount = float(
        input("Enter the amount of money that you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()

    r = rate / 100
    if interest == "simple":
        total_amount = amount * (1 + r * years)
    elif interest == "compound":
        total_amount = amount * math.pow((1 + r), years)
    else:
        print("Invalid input. Please choose either 'simple' or 'compound' for interest calculation.")
        exit()

    print("Total amount after {} years: {:.2f}".format(years, total_amount))

elif user_choice == "bond":

    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    months = int(
        input("Enter the number of months you plan to take to repay the bond: "))

    i = (interest_rate / 100) / 12
    repayment = (i * present_value) / (1 - math.pow(1 + i, -months))

    print("Monthly bond repayment: {:.2f}".format(repayment))
