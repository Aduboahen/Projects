while True:
    try:
        basic = float(input("What is your basic salary? : "))
        break
    except ValueError:
        print("Please enter a number.")

# Additions

while True:
    try:
        allowances = float(
            input("Enter the sum of all allowances received: ")) / 100 * basic
        break
    except ValueError:
        print("Please enter a number.")

gross = basic + allowances

# deductions

ssnit_pf: float = (0.05 * basic) + (0.055 * basic)

taxable_income = gross - ssnit_pf

# income tax

income_tax = 0

chargeable_income = 365

chargeable_income_d = {110: 0.05, 130: 0.1,
                       3_000: 0.175, 16_395: 0.25, 20_000: 0.3}

old_key = 365

key: int
for key, value in chargeable_income_d.items():
    if 0 < taxable_income - chargeable_income >= key:
        income_tax += value * key   
        chargeable_income += key

    elif key > taxable_income - chargeable_income > old_key:
        income_tax += value * (taxable_income - chargeable_income)
    old_key = key

print(f"\nallowances = {allowances}\nincome_tax = {income_tax}")

net_income: float = basic + allowances - ssnit_pf - income_tax

print(f"\nThis is your Net Income(Take Home Salary)\n{net_income}")