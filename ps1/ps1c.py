# # data supplied by the user
# base_annual_salary = float(input('Enter your annual salary: '))
#
# # data that is fixed
# portion_down_payment = 0.25
# rate_of_return = 0.04
# monthly_rate_of_return = rate_of_return / 12
# total_cost = 1000000
# down_payment = total_cost * portion_down_payment
# semi_annual_raise = 0.07
# months = 36
#
# # initially savings are zero. This variable is the core part of the decrementing
# # function used to stop the algorithm
# current_savings = 0.0
#
# # there is an acceptable margin of error for this algorithm
# epsilon = 100
#
# # define high and low bounds for the bisection search
# initial_high = 10000
# high = initial_high
# low = 0
# portion_saved = (high + low) // 2
# steps = 0
#
# # use bisection search to find the solution
# while abs(current_savings - down_payment) > epsilon:
#     steps += 1
#     current_savings = 0.0
#     annual_salary = base_annual_salary
#     monthly_salary = annual_salary / 12
#     monthly_deposit = monthly_salary * (portion_saved / 10000)
#     for month in range(1, months + 1):
#         current_savings *= 1 + monthly_rate_of_return
#         current_savings += monthly_deposit
#         # problem states that semi-annual raises take effect the next month, so
#         # mutate monthly_salary after mutating current_savings
#         if month % 6 == 0:
#             annual_salary *= 1 + semi_annual_raise
#             monthly_salary = annual_salary / 12
#             monthly_deposit = monthly_salary * (portion_saved / 10000)
#     prev_portion_saved = portion_saved
#     if current_savings > down_payment:
#         high = portion_saved
#     else:
#         low = portion_saved
#     # if the solution is outside of the search space on the high bound, low
#     # will eventually equal the inital high value. However, if we use integer
#     # division, low will be one less than high. As such, we round the average
#     # of high and low and cast to an int so that low and high will converge
#     # completely if the solution is outside of the search space on the high
#     # bound
#     portion_saved = int(round((high + low) / 2))
#     # if portion_saved is no longer changing, our search space is no longer
#     # changing (because the search value is outside the search space), so we
#     # break to stop an infinite loop
#     if prev_portion_saved == portion_saved:
#         break
#
# if prev_portion_saved == portion_saved and portion_saved == initial_high:
#     print('It is not possible to pay the down payment in three years.')
# else:
#     print('Best savings rate:', portion_saved / 10000)
#     print('Steps in bisection search:', steps)





################################################################
################################################################

annual_salary = float(input('Enter your starting salary: '))
total_cost = 1000000
semi_annual_raise = 0.07
current_savings = 0
portion_down_payment = 0.25 * total_cost
months = 0
epsilon = 100
low = 0
high = 10000
steps = 0
portion_saved = (low + high) / 2
current_savings = 0

while abs(current_savings - portion_down_payment) > epsilon:
    for mo in range(0, 36):
        monthly_salary = annual_salary / 12
        current_savings = current_savings + float((monthly_salary * portion_saved) / 10000) + (current_savings * 0.04) / 12
        if mo % 6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
    if current_savings > portion_down_payment:
        high = portion_saved
    else:
        low = portion_saved

    portion_saved = int(round((high + low) / 2))
    steps += 1

print('Best savings rate:', portion_saved / 10000)
print('Steps in bisection search:', steps)