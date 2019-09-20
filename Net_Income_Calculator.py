basic = float(input("What is your basic salary? : \n"))

#Additions
risk_allowance = (0.3 * basic)
overtime_allowance = (0.15 * basic)

#Subtractions
ssnit = (0.055 * basic)

first_132 = (basic - 132)
next_66 = (first_132) * 0.05
next_92 = (first_132 - next_66) * 0.1

income_tax =  (next_66 + next_92)
providence = (float(input("Percentage contributed to Providence Insurance : \n"))/100) * basic
              
net_income =  basic + (risk_allowance + overtime_allowance) - (ssnit+ income_tax + providence)

print(f"This is your Net Income(Take Home Salary) \n {net_income}")
