annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: " ))
total_cost = float(input("Enter the cost of your dream home: "))

monthly_savings = (annual_salary*portion_saved)/12
portion_down_payment = 0.25*total_cost
r = 0.04
current_savings = 0
month = 0


while current_savings <= portion_down_payment:
    current_savings = current_savings + (current_savings*r)/12 + monthly_savings
    month = month + 1
    year = month // 12
    months_remainder = (month % 12)


print('It will take {} years and {} months to earn the down-payment for your dream house'
      .format(year, months_remainder))
