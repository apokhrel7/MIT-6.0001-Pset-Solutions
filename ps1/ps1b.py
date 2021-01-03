annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter the percent of your salary to  save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter semi-annual salary raise as a decimal: "))

portion_down_payment = 0.25 * total_cost
r = 0.04
monthly_savings = (annual_salary * portion_saved) / 12

month = 0
current_savings = 0

while current_savings <= portion_down_payment:
    monthly_savings = (annual_salary * portion_saved) / 12
    current_savings = current_savings + (current_savings*r)/12 + monthly_savings
    month = month+1
    if month % 6 == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)

print("It takes", month, "months to save up for the down payment of your dream house")
