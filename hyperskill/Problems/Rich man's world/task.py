initial_sum = int(input())
result_sum = initial_sum
protected_sum = 700000
interest_rate = 0.071
number_of_years = 0
while result_sum <= protected_sum:
    number_of_years += 1
    result_sum += result_sum * interest_rate
print(number_of_years)
