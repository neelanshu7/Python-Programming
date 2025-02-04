class Textile:
    def __init__(self):
        # Initialize attributes for Textile
        self.type = ''
        self.size = ''
        self.colour = ''
        self.qty_on_hand = 0
        self.rate = 0.0

    def getDet(self):
        # Get values of attributes from the user
        self.type = input("Enter Textile Type: ")
        self.size = input("Enter Textile Size: ")
        self.colour = input("Enter Textile Colour: ")
        self.qty_on_hand = int(input("Enter Quantity on Hand: "))
        self.rate = float(input("Enter Rate per Unit: "))

    def putDet(self):
        # Print details of the Textile object
        print(f"Type: {self.type}")
        print(f"Size: {self.size}")
        print(f"Colour: {self.colour}")
        print(f"Quantity on Hand: {self.qty_on_hand}")
        print(f"Rate per Unit: {self.rate}")


# This is the separate module function to handle textile objects
def store_textiles_and_calculate_sales(textile_objects):
    # Dictionary to store textile objects
    Textile_dict = {}
    total_sales_amount = 0

    # Store objects in dictionary and calculate total sales amount
    for i, textile in enumerate(textile_objects):
        Textile_dict[f'Textile {i+1}'] = textile
        total_sales_amount += textile.qty_on_hand * textile.rate

    # Print details of all textile objects
    for key, textile in Textile_dict.items():
        print(f"\nDetails of {key}:")
        textile.putDet()

    # Print total sales amount
    print(f"\nTotal Sales Amount: {total_sales_amount}")


# Example usage
if __name__ == "__main__":
    # Get the number of textiles
    num_textiles = int(input("Enter the number of textiles: "))
    textile_list = []

    # Get details for each textile and store them in a list
    for _ in range(num_textiles):
        textile = Textile()
        textile.getDet()
        textile_list.append(textile)

    # Pass the list of textiles to the function for processing
    store_textiles_and_calculate_sales(textile_list)
