# first number is number of toys available
# second number is budget
number_of_toys, budget = input().strip().split(' ')
number_of_toys = int(number_of_toys)
budget = int(budget)
print(number_of_toys)
print(budget)

# second lines are list of toy prices
toy_prices = input().strip().split(' ')
toy_prices.sort(key=lambda x: int(x))
result = 0
for price in toy_prices:
    price = int(price)
    if price < budget:
        result += 1
        budget -= price
    if budget <= 0:
        break
print(result)
