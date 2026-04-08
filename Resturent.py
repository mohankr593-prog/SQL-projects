menu = {
    'pizza': 99.99,
    'pasta': 79.99,
    'salad': 49.99,
    'dessert': 39.99,
    'drink': 19.99,
    'burger': 89.99,
    'fries': 29.99,
    'soup': 59.99,
    'momos': 69.99,
    'steak': 129.99,
    'sandwich': 59.99,
    'ice cream': 29.99,
    'coffee': 19.99,
    'tea': 14.99,
    'juice': 24.99,
    'smoothie': 34.99,
    'cocktail': 49.99,
    'wine': 99.99,
}

# Define combos with discount rate
combos = [
    (['pizza', 'drink'], 0.05),
    (['burger', 'fries', 'drink'], 0.05),
    (['steak', 'wine'], 0.05),
    (['dessert', 'coffee'], 0.05)  # example of overlapping combo
]

print("Welcome to the ATFS Restaurant!")
print("Any Time Food Service")
print("Type 'done' when you finish ordering.\n")

# Display menu
print("Menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: ${price:.2f}")

order = {}

# Function to suggest combos in real time
def suggest_combos(order):
    suggestions = []
    for combo_items, _ in combos:
        missing_items = [i for i in combo_items if i not in order or order[i] == 0]
        if 0 < len(missing_items) < len(combo_items):
            suggestions.append(f"Add {', '.join(missing_items)} to get a combo discount!")
    return suggestions

# Take orders
while True:
    item = input("\nEnter the item you want to order (or 'done' to finish): ").lower().strip()
    
    if item == 'done':
        break
    elif item in menu:
        while True:
            try:
                quantity = int(input(f"How many {item.capitalize()} would you like? "))
                if quantity > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        order[item] = order.get(item, 0) + quantity
        print(f"{quantity} x {item.capitalize()} added to your order.")
        
        # Suggest combos after adding item
        for suggestion in suggest_combos(order):
            print("💡 Suggestion:", suggestion)
            
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")

if not order:
    print("You did not order anything. Goodbye!")
    exit()

# Calculate total
total = sum(menu[item] * quantity for item, quantity in order.items())

# Function to calculate maximum combo discounts
def calculate_combo_discounts(order):
    total_discount = 0
    applied_combos = []
    remaining_order = order.copy()
    
    # Keep applying combos while possible
    while True:
        applied = False
        for combo_items, discount_rate in combos:
            if all(remaining_order.get(item, 0) > 0 for item in combo_items):
                combo_total = sum(menu[item] for item in combo_items)
                discount_amount = combo_total * discount_rate
                total_discount += discount_amount
                applied_combos.append((combo_items, discount_amount))
                # Reduce count for items used in combo
                for item in combo_items:
                    remaining_order[item] -= 1
                applied = True
        if not applied:
            break
    
    return total_discount, applied_combos

combo_discount, applied_combos = calculate_combo_discounts(order)
total -= combo_discount

# Apply extra 10% discount if total > $200
extra_discount = 0
if total > 200:
    extra_discount = total * 0.10
    total -= extra_discount

# Print final summary
print("\nYour order summary:")
for item, quantity in order.items():
    print(f"- {item.capitalize()} x {quantity}: ${menu[item] * quantity:.2f}")

if applied_combos:
    print("\nCombo discounts applied:")
    for combo_items, discount_amount in applied_combos:
        print(f"- {', '.join([i.capitalize() for i in combo_items])}: -${discount_amount:.2f}")

if extra_discount > 0:
    print(f"\nExtra 10% discount for orders over $200: -${extra_discount:.2f}")

print(f"\nTotal to pay: ${total:.2f}")
print("Thank you for dining with us!")
    
   
