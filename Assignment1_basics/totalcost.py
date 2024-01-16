# A store charges ₹120 per item if you buy less than 10 items. If you buy between 10
# and 99 items, the cost is ₹100 per item. If you buy 100 or more items, the cost is ₹70
# per item. Write a program that asks the user how many items they are buying and prints
# the total cost.
items = int(input("Enter the number of items you have purchased: "))
if items < 10:
    price_per_item = 120
elif items < 100:
    price_per_item = 100
else:
    price_per_item = 70
total_cost = price_per_item * items
print("The total cost : ", total_cost)