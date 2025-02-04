class EB_amount:
    def __init__(self):
        # Initialize data members
        self.units_used = 0
        self.bill = 0

    def inputdetail(self, units):
        # Set units_used from parameter
        self.units_used = units

    def calculate(self):
        # Calculate the bill based on units used
        if self.units_used <= 100:
            self.bill = 0
        elif self.units_used <= 200:
            self.bill = (self.units_used - 100) * 3
        elif self.units_used <= 500:
            self.bill = (100 * 0) + (100 * 3) + (self.units_used - 200) * 4
        else:
            self.bill = (100 * 0) + (100 * 3) + (300 * 4) + (self.units_used - 500) * 5

    def writetofile(self, file):
        # Write consumer details to file
        file.write(f"Units used: {self.units_used}\n")
        file.write(f"Bill amount: {self.bill}\n\n")

# Function to process multiple consumers and write their details to a file
def process_consumers(n, units_list):
    with open('EB_Bills.txt', 'w') as file:
        for i in range(n):
            consumer = EB_amount()
            consumer.inputdetail(units_list[i])
            consumer.calculate()
            consumer.writetofile(file)
        print(f"Details of {n} consumers written to 'EB_Bills.txt'.")

# Sample input/output for demonstration
num_consumers = int(input("Enter the number of consumers: "))
units_list = []
for i in range(num_consumers):
    units = int(input(f"Enter the number of units used by the customer {i+1}: "))
    units_list.append(units)

process_consumers(num_consumers, units_list)


'''
class EB_amount:
    # Constructor to initialize units_used and bill to zero
    def __init__(self):
        self.units_used = 0
        self.bill = 0
    
    # Method to get input for units_used
    def inputdetail(self):
        self.units_used = int(input("Enter the units used: "))
    
    # Method to calculate the bill amount based on the units used
    def calculate(self):
        if self.units_used <= 200:
            self.bill = self.units_used * 3
        elif 201 <= self.units_used <= 500:
            self.bill = (200 * 3) + ((self.units_used - 200) * 4)
        else:
            self.bill = (200 * 3) + (300 * 4) + ((self.units_used - 500) * 5)
    
    # Method to print the bill amount and units used
    def Printdetail(self):
        print(f"Units used: {self.units_used}")
        print(f"Bill amount: {self.bill} rupees")


# Example of how to use the class
consumer = EB_amount()
consumer.inputdetail()
consumer.calculate()
consumer.Printdetail()

'''