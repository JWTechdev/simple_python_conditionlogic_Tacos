coffee_sizes = {'Small', 'Medium', 'Large'}

coffee_prices = {}
price = 1.50
for cup in coffee_sizes:
    coffee_prices[cup] = price
    price = price + 1

print(coffee_prices)