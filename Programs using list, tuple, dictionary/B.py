# Define a dictionary to store item details
item_inventory = {
    '001': {'name': 'Apple', 'price': 0.5, 'quantity': 100},
    '002': {'name': 'Banana', 'price': 0.3, 'quantity': 150},
    '003': {'name': 'Cherry', 'price': 1.0, 'quantity': 50}
}

# Initialize an empty shopping cart
shopping_cart = []

def add_item_to_cart(item_code, quantity):
    if item_code in item_inventory:
        item = item_inventory[item_code]
        if quantity > item['quantity']:
            print(f"Error: Not enough {item['name']} in stock.")
            return
        
        # Check if item is already in the cart
        for cart_item in shopping_cart:
            if cart_item['code'] == item_code:
                cart_item['quantity'] += quantity
                item['quantity'] -= quantity
                print(f"Updated {item['name']} quantity to {cart_item['quantity']}.")
                return
        
        # Add new item to the cart
        shopping_cart.append({'code': item_code, 'quantity': quantity})
        item['quantity'] -= quantity
        print(f"Added {item['name']} to the cart.")
    else:
        print("Error: Item code not found.")

def view_cart_contents():
    if not shopping_cart:
        print("The cart is empty.")
        return
    
    print("\nCart Contents:")
    for cart_item in shopping_cart:
        item = item_inventory[cart_item['code']]
        total_price = cart_item['quantity'] * item['price']
        print(f"Item: {item['name']}, Price: ${item['price']:.2f}, Quantity: {cart_item['quantity']}, Total: ${total_price:.2f}")
    print()

def remove_item_from_cart(item_code):
    global shopping_cart
    for cart_item in shopping_cart:
        if cart_item['code'] == item_code:
            item = item_inventory[item_code]
            item['quantity'] += cart_item['quantity']
            shopping_cart = [i for i in shopping_cart if i['code'] != item_code]
            print(f"Removed {item['name']} from the cart.")
            return
    print("Error: Item not found in the cart.")

def calculate_total_cost():
    total_cost = 0
    for cart_item in shopping_cart:
        item = item_inventory[cart_item['code']]
        total_cost += cart_item['quantity'] * item['price']
    return total_cost

def display_menu():
    print("\nShopping Cart Management System")
    print("1. Add item to cart")
    print("2. View cart contents")
    print("3. Remove item from cart")
    print("4. Calculate total cost")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item_code = input("Enter item code: ")
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    raise ValueError("Quantity must be a positive integer.")
                add_item_to_cart(item_code, quantity)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            view_cart_contents()
        
        elif choice == '3':
            item_code = input("Enter item code to remove: ")
            remove_item_from_cart(item_code)
        
        elif choice == '4':
            total_cost = calculate_total_cost()
            print(f"Total cost of items in the cart: ${total_cost:.2f}")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
