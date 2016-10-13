import math

total = 0
prices_of_tacos = [7.00, 5.00, 11.00, 13.00, 15.00]

for price in prices_of_tacos:
    print('Price is', price)
    total = total + price
    print('total is', total)

average = total / len(prices_of_tacos)
print('avg is', average)
