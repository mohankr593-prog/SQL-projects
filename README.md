# SQL- 1st projects
menu = {
    'pizza': 99.99,
    'pasta': 79.99,
    'salad': 49.99,
    'dessert': 39.99,
    'drink': 19.99,
    'burger' : 89.99,
    'fries' : 29.99,
    'soup' : 59.99,
    'momos' : 69.99,
    'steak' : 129.99,
    'sandwich' : 59.99,
    'ice cream' : 29.99,
    'coffee' : 19.99,
    'tea' : 14.99,
    'juice' : 24.99,
    'smoothie' : 34.99,
    'cocktail' : 49.99,
    'wine' : 99.99,

}
print("Welcome to the ATFS Restaurant!")
print("Any Time Food Service")
print("Instructions: Type the name of the item you want to order. Type 'done' when you are finished.")
print("Here is the menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: ${price:.2f}")
order = []
while True:
    item = input("Enter the item you want to order (or 'done' to finish): ").lower()
    if item == 'done':
        break
    elif item in menu:
        order.append(item)
        print(f"{item.capitalize()} added to your order.")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")
if not order:
    print("You did not order anything. Goodbye!")
    exit()
total = sum(menu[item] for item in order)
print("\nYour order summary:")
for item in order:
    print(f"- {item.capitalize()}: ${menu[item]:.2f}")
print(f"Total: ${total:.2f}")
print("Thank you for dining with us!")
    
   
