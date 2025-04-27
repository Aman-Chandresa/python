food_items = [("Pizza", 349), ("Burger", 179), ("Pasta", 299), ("Double Cheese Burger", 249), ("French Fries", 199)]

sorted_food_items = sorted(food_items, key=lambda item: item[1], reverse=True)

print("Food items sorted by price in descending order:", sorted_food_items)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")