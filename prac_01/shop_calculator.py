"""
CP1404 - Practical 1
Shop calculator program to determine total (discounted) price
"""

total_price = 0
total_items = int(input("Number of items: "))
while total_items < 0:
    print("Invalid number of items!")
    total_items = int(input("Number of items: "))
for item in range(total_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

# Applying the 10% discount
if total_price > 100:
    total_price *= 0.9

print(f"Total price for {total_items} items is ${total_price:.2f}")


