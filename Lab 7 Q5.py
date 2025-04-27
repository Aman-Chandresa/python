prices = {
    "Orange": 80,
    "Papaya": 60,
    "Mango": 70,
    "Watermelon": 35
}

quantity = {
    "Orange": 1,
    "Papaya": 2,
    "Mango": 6,
    "Watermelon": 5
}

total_bill = sum(prices[item] * quantity[item] for item in prices)
print("Total bill: ₹", total_bill)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")