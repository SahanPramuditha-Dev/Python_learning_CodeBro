menu = {
    "pizza": 3.00,
    "burger": 2.50,
    "fries": 1.00,
    "soda": 1.50,
    "salad": 2.00,
    "chips": 1.50,
    "lemonade": 1.50,
    "skittles": 2.75,
    "hot dogs": 2.50
}

cart = []
total = 0

print("-------- MENU --------")
for food, price in menu.items():
    print(f"{food.title():10} : $ {price:.2f}")

while True:
    food = input("\nEnter a food to buy (q to quit): ").lower()

    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        print(f"{food.title()} added to cart.")
    else:
        print("Item not on menu.")

print("\n--------- YOUR CART ---------")

if cart:
    for food in cart:
        print(f"{food.title():10} : $ {menu[food]:.2f}")
        total += menu[food]

    print("-----------------------------")
    print(f"Total: $ {total:.2f}")
else:
    print("Your cart is empty.")

print("------------------------------")
